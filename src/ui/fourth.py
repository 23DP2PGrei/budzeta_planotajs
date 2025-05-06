import tkinter as tk
from src.ui.fifth_yes import open_savings_input_window
from src.ui.fifth_no import open_results_window
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BUTTON_BG, BG_COLOR

def open_savings_goal_window(previous_window, income, spending_data, user_id, month):
    previous_window.destroy()

    fourth = tk.Tk()
    fourth.title("Savings Goal")
    fourth.geometry(f"{WIDTH}x{HEIGHT}")
    fourth.resizable(False, False)
    fourth.configure(bg=BG_COLOR)

    # Galvenais virsraksts
    tk.Label(fourth, text="Budget Planner", font=("Arial", 24, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(30, 10))

    # Jautājums par uzkrājumu mērķi
    tk.Label(fourth, text="Do you have\na savings goal?",
             font=("Arial", 18, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR, justify="center").pack(pady=(20, 20))

    # Pogu rāmis
    button_frame = tk.Frame(fourth, bg=BG_COLOR)
    button_frame.pack()

    # Ja atbild "Yes", pāriet uz uzkrājumu mērķa ievadi
    def on_yes():
        open_savings_input_window(fourth, income, spending_data, user_id, month)

    # Ja atbild "No", iet uz rezultātiem
    def on_no():
        open_results_window(fourth, income, spending_data, user_id, month)
    
    # Poga "Yes"
    yes_button = tk.Button(button_frame, text="Yes", font=("Arial", 14),
                           bg=BUTTON_BG, fg=TEXT_COLOR, bd=1, width=8, command=on_yes)
    yes_button.grid(row=0, column=0, padx=10)

    # Poga "No"
    no_button = tk.Button(button_frame, text="No", font=("Arial", 14),
                          bg=BUTTON_BG, fg=TEXT_COLOR, bd=1, width=8, command=on_no)
    no_button.grid(row=0, column=1, padx=10)

    fourth.mainloop() # Sāk loga ciklu