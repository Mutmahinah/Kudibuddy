import random

tips = [
    "No dey chop all your money finish — try save small every month.",
    "If you dey earn 100 naira, plan am like say you dey earn 70 naira.",
    "Emergency fit happen anytime — try get small backup (emergency fund).",
    "Use budget like map — e go help you reach where your money suppose go.",
    "Abeg, no dey borrow if you no get clear plan to pay back.",
    "Cut your coat according to your material, not according to your style.",
    "Small small cut down on ‘soft life’, make future sweet pass today.",
    "Make you dey track wetin you dey buy — small small things dey chop big money.",
    "Try buy things wey go help you grow (like books or small business tools).",
    "No use peer pressure take enter wahala — shine your eye.",
    "Person wey dey save no dey broke, even when salary delay.",
    "Avoid 'debt trap' — make credit card or loan no be your padi.",
    "Invest in small things wey go return better gain, like knowledge or business.",
    "Your budget no suppose dey fight with your goals — align am.",
]

def get_random_tip():
    return random.choice(tips)
