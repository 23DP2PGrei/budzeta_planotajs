import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data.data import save_data_to_csv
from src.settings.apreikins import calculate_balance, calculate_total_spent
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BG_COLOR

def open_results_window(previous_window, income, spending_data, user_id, month):
    previous_window.destroy()

    total_spent = calculate_total_spent(spending_data)
    balance = calculate_balance(income, total_spent)

    file_path = "data/budget_data.csv"
    save_data_to_csv(file_path, user_id, month, income, spending_data, balance)

    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    categories = list(spending_data.keys())
    values = list(spending_data.values())

    ax.pie(values, labels=categories, startangle=90,
           textprops={'fontsize': 8, 'color': TEXT_COLOR},
           autopct='%1.1f%%')
    ax.axis('equal')
    ax.text(0, 0, f"{sum(values)}€", ha='center', va='center',
            fontsize=16, fontweight='bold', color=TEXT_COLOR)

    fifth = tk.Tk()
    fifth.title("Budget Summary")
    fifth.geometry(f"{WIDTH}x{HEIGHT}")
    fifth.configure(bg=BG_COLOR)

    tk.Label(fifth, text="Budget Planner", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(20, 5))
    canvas = FigureCanvasTkAgg(fig, master=fifth)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    balance_text = f"Balance: {balance}€"
    tk.Label(fifth, text=balance_text, font=("Arial", 14), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(10, 5))

    tk.Button(fifth, 
              text="Done", 
              font=("Arial", 12, "bold"),
              fg=TEXT_COLOR, 
              bg=BG_COLOR, 
              bd=0,
              highlightthickness=0, 
              command=fifth.destroy).place(relx=0.95, rely=0.97, anchor="se")

    fifth.mainloop()