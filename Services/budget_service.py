import csv
import os 

CSV_FILE = "Data/data.csv"

def pievieno(user_id, month, income, food, entertainment, healthcare, loan_payments, rent, savings_goal):
    if extra_expenses is None:
        extra_expenses = {}

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            header = ["User ID", "Month", "Income", "Food", "Entertainment", "Healthcare", "Loan Payments", "Rent", "Savings Goal"]
            header.extend(extra_expenses.keys()) 
            writer.writerow(header)

        row = [user_id, month, income, food, entertainment, healthcare, loan_payments, rent, savings_goal]
        row.extend(extra_expenses.values())

        writer.writerow(row)

def nolasa():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data