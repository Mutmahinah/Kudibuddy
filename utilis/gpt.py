import google.generativeai as genai
import streamlit as st
import random

# Set up Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_gpt_tip(pidgin=False):
    today = datetime.today().strftime("%Y-%m-%d")
    prompt = random.choice([
        f"Give a personal finance tip about saving money ({today}).",
        f"Provide investment wisdom for long-term wealth ({today}).",
        f"Suggest a budgeting trick for managing expenses wisely ({today}).",
        f"Offer financial advice on avoiding debt ({today}).",
        f"Share a smart money habit for financial independence ({today})."
    ])

    if pidgin:
        prompt += " in Nigerian Pidgin English"

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return response.text.strip()

def generate_goal_encouragement(goal, pidgin=False):
    prompt = f"Give me a motivational message to help someone stay focused on saving for {goal}."
    if pidgin:
        prompt += " Write it in Nigerian Pidgin English."

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    return response.text.strip()

def generate_gpt_feedback(prompt):
    system_message = "You are a friendly Nigerian financial coach who speaks Pidgin English and encourages users to manage money wisely."
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"{system_message}\n\n{prompt}")

    return response.text.strip() 

def generate_daily_financial_advice():
    """
    Generates financial advice using AI and provides it in both English & Pidgin.
    """
    prompt_english = "Give a powerful financial advice that inspires good money habits."
    prompt_pidgin = "Give a powerful financial advice that inspires good money habits in Nigerian Pidgin English."

    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Generate English advice
    response_eng = model.generate_content(prompt_english)
    advice_english = response_eng.text.strip()

    # Generate Pidgin advice
    response_pidgin = model.generate_content(prompt_pidgin)
    advice_pidgin = response_pidgin.text.strip()

    return {"english": advice_english, "pidgin": advice_pidgin}
