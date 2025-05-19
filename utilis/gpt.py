import google.generativeai as genai
import streamlit as st

# Set up Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_gpt_tip(pidgin=False):
    prompt = "Give me a short personal finance tip"
    if pidgin:
        prompt += " in Nigerian Pidgin English"

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip()

def generate_goal_encouragement(goal, pidgin=False):
    prompt = f"Give me a motivational message to help someone stay focused on saving for {goal}."
    if pidgin:
        prompt += " Write it in Nigerian Pidgin English."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip()

def generate_gpt_feedback(prompt):
    system_message = "You are a friendly Nigerian financial coach who speaks Pidgin English and encourages users to manage money wisely."
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"{system_message}\n\n{prompt}")

    return response.text.strip()
