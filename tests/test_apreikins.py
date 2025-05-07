import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.settings.apreikins import (
    calculate_total_spent,
    calculate_balance,
    calculate_savings_plan
)

def test_calculate_total_spent():
    spending = {"Food": 100, "Rent": 200, "Other": 50}
    assert calculate_total_spent(spending) == 350

def test_calculate_balance():
    assert calculate_balance(1000, 600) == 400

def test_calculate_savings_plan_enough_balance():
    goal = 600
    time = 3
    income = 1000
    spending = {"Rent": 300, "Food": 100}
    monthly_goal, shortage, balance = calculate_savings_plan(goal, time, income, spending)
    assert monthly_goal == 200
    assert balance == 600
    assert shortage <= 0