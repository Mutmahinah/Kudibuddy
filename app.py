import streamlit as st
from utilis.budget import calculate_budget, suggest_saving_plan
from utilis.tips import get_random_tip
from utilis.gpt import generate_gpt_tip, generate_goal_encouragement, generate_daily_financial_advice


st.set_page_config(page_title="KudiBuddy", layout="centered")

# --- Sidebar Personalization ---
st.sidebar.title("🧑 Personalize")
user_name = st.sidebar.text_input("Your Name", "Tolu")
show_avatar = st.sidebar.checkbox("Show Avatar", True)

st.title("💸 KudiBuddy - Your Personal Money Pal")

if show_avatar:
    st.image("https://i.imgur.com/1X4qkhd.png", width=80)

st.markdown(f"### 👋 Welcome, **{user_name}**!")
st.markdown("You're doing amazing with your savings. Let’s keep the streak alive!")

# --- Budget Breakdown ---
st.header("📊 Budget Breakdown")

income = st.number_input("Enter your monthly income (₦):", min_value=0)
expenses = st.text_area("Enter your expenses (e.g., rent: 20000, food: 15000):")

if st.button("Generate Budget"):
    try:
        # Improved expense parsing with better error handling
        exp_dict = {k.strip(): int(v.strip()) for item in expenses.split(',') if ':' in item for k, v in [item.split(':', 1)]}
        result = calculate_budget(income, exp_dict)
        
        st.success(
            f"🧾 **Budget Breakdown:**\n\n"
            f"✅ Essentials: ₦{result['essentials']}\n"
            f"💰 Savings: ₦{result['savings']}\n"
            f"🎭 Flex Spending: ₦{result['flex']}"
        )
    except ValueError:
        st.error("⚠️ Format your expenses correctly. Example: rent: 20000, food: 15000")
    
    st.info(f"💡 Tip of the day: {get_random_tip()}")

# --- Savings Goal Planner ---
st.header("🎯 Savings Goal Planner")

goal_name = st.text_input("Your savings goal (e.g., New phone)")
goal_amount = st.number_input("Goal amount (₦):", min_value=0)
weeks = st.number_input("Weeks to achieve this goal:", min_value=1)

pidgin_toggle = st.toggle("Use Nigerian Pidgin")

if st.button("Calculate Weekly Savings"):
    if goal_amount > 0 and weeks > 0:
        weekly_savings = suggest_saving_plan(goal_amount, weeks)
        st.success(f"To achieve '{goal_name}', save ₦{weekly_savings} weekly.")
        
        # Savings progress tracking
        current_savings = st.slider("How much have you saved so far?", 0, int(goal_amount), step=1000)
        progress = min(current_savings / goal_amount, 1.0)
        st.progress(progress)
        st.caption(f"💰 You’ve saved ₦{current_savings} out of ₦{goal_amount}")

        # Use caching to optimize API calls
        @st.cache_resource
        def cached_goal_encouragement(goal, pidgin):
            return generate_goal_encouragement(goal, pidgin)

        encouragement = cached_goal_encouragement(goal_name, pidgin_toggle)
        st.markdown(f"🫂 **Encouragement:** _{encouragement}_")
    else:
        st.error("⚠️ Please enter a valid goal amount and timeframe.")

# --- AI Money Tip ---
import random
from datetime import datetime

st.header("✨ Smarter Money Tip")

use_gpt = st.toggle("Get an AI-generated tip")

if use_gpt:
    # Generate a fresh prompt each time
    
    gpt_tip = generate_gpt_tip(pidgin=pidgin_toggle)
    
    st.markdown(f"🧠 AI Tip: {gpt_tip}", unsafe_allow_html=True)


st.header("📖 Ask for Daily Financial Wisdom")

# Button to request AI-generated financial advice
if st.button("Get Today's Financial Advice"):
    daily_wisdom = generate_daily_financial_advice()
    st.markdown(f"💡 **Financial Wisdom (English):** _{daily_wisdom['english']}_")
    st.markdown(f"💡 **Financial Wisdom (Pidgin):** _{daily_wisdom['pidgin']}_")
