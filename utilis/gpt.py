# -*- coding: utf-8 -*-
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_gpt_tip(pidgin=False):
    prompt = "Give me a short personal finance tip"
    if pidgin:
        prompt += " in Nigerian Pidgin English"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def generate_goal_encouragement(goal, pidgin=False):
    prompt = f"Give me a motivational message to help someone stay focused on saving for {goal}."
    if pidgin:
        prompt += " Write it in Nigerian Pidgin English."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_gpt_feedback(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly Nigerian financial coach who speaks Pidgin English and encourages users to manage money wisely."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

    return response.choices[0].message.content.strip()
