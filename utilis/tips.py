# -*- coding: utf-8 -*-
import random

tips = [
    "Track wetin you dey spend every week.",
    "No dey buy wetin you no need — na so money dey waka.",
    "Always try save at least 10% of your income.",
    "Put your money for something wey go grow am.",
    "E good make you get emergency fund — wahala no dey tell person."
]

def get_random_tip():
    return random.choice(tips)
