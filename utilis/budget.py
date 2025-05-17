# -*- coding: utf-8 -*-
def calculate_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses

    essentials = int(0.5 * remaining)
    savings = int(0.3 * remaining)
    flex = remaining - (essentials + savings)

    return {
        "essentials": essentials,
        "savings": savings,
        "flex": flex
    }

def suggest_saving_plan(goal_amount, weeks):
    return round(goal_amount / weeks, 2)
