import tkinter as tk
from src.settings.apreikins import calculate_savings_plan
from src.ui.seventh_yes import open_results_window_last
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BG_COLOR
from src.settings.next_button import create_next_button

def open_savings_plan_window(previous_window, goal, time, income, spending_data, user_id, month):
    previous_window.destroy()

    # Aprēķina, cik vajag katru mēnesi uzkrāt, cik pietrūkst, un bilanci
    monthly_goal, shortage, balance = calculate_savings_plan(goal, time, income, spending_data)

    sixth = tk.Tk()
    sixth.title("Savings Plan")
    sixth.geometry(f"{WIDTH}x{HEIGHT}")
    sixth.configure(bg=BG_COLOR)

    # Virsraksts
    tk.Label(sixth, text="Budget Planner", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(30, 10))

    # Informācijas rāmis
    info_frame = tk.Frame(sixth, bg=BG_COLOR)
    info_frame.pack(pady=10, anchor="w", padx=20)

    # Palīgfunkcija info rindām
    def add_info(label_text, value_text, color=TEXT_COLOR):
        tk.Label(info_frame, text=label_text, font=("Arial", 14, "bold"),
                 fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w")
        tk.Label(info_frame, text=value_text, font=("Arial", 13),
                 fg=color, bg=BG_COLOR).pack(anchor="w", pady=(0, 10))

    # Informācija par mērķi
    add_info("Your savings goal:", f"{goal}€")
    add_info("Time:", f"{time} months")
    add_info("Amount to save each month:", f"{monthly_goal}€")

    # Statuss: vai pietiek naudas mērķim
    if balance >= monthly_goal:
        add_info("Savings status:", "You can reach your goal!", color="green")
    else:
        add_info("Savings status:", f"You need {shortage}€ more", color="red")

    # Poga uz nākamo logu
    next_button = create_next_button(sixth, lambda: open_results_window_last(
        sixth, income, spending_data, user_id, month))
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    sixth.mainloop()