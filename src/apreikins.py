def calculate_total_spent(spending_data):
    return sum(spending_data.values())

def calculate_balance(income, total_spent):
    return int(income) - total_spent

def get_spending_data(category_entries):
    data = {}
    for label, entry in category_entries:
        name = label.cget("text")
        try:
            amount = int(entry.get())
        except ValueError:
            amount = 0
        data[name] = amount
    return data

def calculate_savings_plan(goal, time, income, spending_data):
    total_spent = calculate_total_spent(spending_data)
    balance = calculate_balance(income, total_spent)
    monthly_goal = goal // time
    shortage = monthly_goal - balance
    return monthly_goal, shortage, balance