import streamlit as st
from utils.budget import calculate_budget, suggest_saving_plan
from utils.tips import get_random_tip
from utils.gpt import generate_gpt_tip, generate_goal_encouragement

st.set_page_config(page_title="KudiBuddy", layout="centered")

# --- Personalization ---
st.sidebar.title("🧑 Personalize")
user_name = st.sidebar.text_input("Your Name", "Tolu")
show_avatar = st.sidebar.checkbox("Show Avatar", True)

st.title("💸 KudiBuddy - Your Personal Money Pal")

if show_avatar:
    st.image("https://i.imgur.com/1X4qkhd.png", width=80)

st.markdown(f"### 👋 Welcome, **{user_name}**!")
st.markdown("You're doing amazing with your savings. Let’s keep the streak alive!")

# --- Income & Expense ---
st.header("📊 Budget Breakdown")

income = st.number_input("Enter your monthly income (₦):", min_value=0)
expenses = st.text_area("Enter your expenses (e.g., rent: 20000, food: 15000):")

if st.button("Generate Budget"):
    try:
        exp_dict = dict(item.strip().split(':') for item in expenses.split(',') if ':' in item)
        exp_dict = {k: int(v.strip()) for k, v in exp_dict.items()}
        result = calculate_budget(income, exp_dict)
        st.success(
            f"🧾 Budget Breakdown:\n\n"
            f"**Essentials:** ₦{result['essentials']}\n\n"
            f"**Savings:** ₦{result['savings']}\n\n"
            f"**Flex:** ₦{result['flex']}"
        )
    except Exception as e:
        st.error("Please format your expenses correctly. E.g., rent: 20000, food: 10000")

    st.info("💡 Tip of the day: " + get_random_tip())

# --- Goal Section ---
st.header("🎯 Savings Goal Planner")

goal_name = st.text_input("What's your savings goal? (e.g., New phone)")
goal_amount = st.number_input("Goal amount (₦):", min_value=0)
weeks = st.number_input("Weeks to achieve this goal:", min_value=1)

pidgin_toggle = st.toggle("Use Nigerian Pidgin for GPT responses")

if st.button("Calculate Weekly Savings"):
    weekly_savings = suggest_saving_plan(goal_amount, weeks)
    st.success(f"To achieve '{goal_name}', save ₦{weekly_savings} weekly.")

    # Progress simulation
    current_savings = st.slider("How much have you saved so far?", 0, int(goal_amount), step=1000)
    progress = min(current_savings / goal_amount, 1.0)
    st.progress(progress)
    st.caption(f"You’ve saved ₦{current_savings} out of ₦{goal_amount}")

    encouragement = generate_goal_encouragement(goal_name, pidgin=pidgin_toggle)
    st.markdown(f"🫂 **Encouragement:** _{encouragement}_")

# --- AI Tip Section ---
st.header("✨ Smarter Money Tip")

use_gpt = st.toggle("Get an AI-generated tip")

if use_gpt:
    gpt_tip = generate_gpt_tip(pidgin=pidgin_toggle)
    st.markdown(f"""
    <div style='background-color:#f9f9f9;padding:15px;border-left:5px solid #00a;'>
        <strong>🧠 GPT Tip:</strong><br>{gpt_tip}
    </div>
    """, unsafe_allow_html=True)
