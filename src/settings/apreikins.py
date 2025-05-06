def calculate_total_spent(spending_data):
    return sum(spending_data.values()) # Saskaita visus izdevumus

def calculate_balance(income, total_spent):
    return int(income) - total_spent # Aprēķina bilanci: ienākumi - izdevumi

def get_spending_data(category_entries):
    data = {}
    for label, entry in category_entries:
        name = label.cget("text") # Iegūst kategorijas nosaukumu no Label
        try:
            amount = int(entry.get()) # Mēģina pārvērst ievadi par skaitli
        except ValueError:
            amount = 0 # Ja nav derīgs skaitlis, pieņem ka 0
        data[name] = amount 
    return data # Atgriež vārdnīcu {kategorija: summa}

def calculate_savings_plan(goal, time, income, spending_data):
    total_spent = calculate_total_spent(spending_data)
    balance = calculate_balance(income, total_spent)
    monthly_goal = goal // time # Aprēķina, cik jākrāj katru mēnesi
    shortage = monthly_goal - balance # Aprēķina, vai pietiek atlikuma
    return monthly_goal, shortage, balance