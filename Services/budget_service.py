import csv
import os 

CSV_FILE = "Data/data.csv"

def pievieno(user_id, month, income, food, entertainment, healthcare, loan_payments, rent, savings_goal):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, month, income, food, entertainment, healthcare, loan_payments, rent, savings_goal])

def nolasa():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data