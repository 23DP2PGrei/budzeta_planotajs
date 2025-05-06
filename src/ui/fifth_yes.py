import tkinter as tk
from src.ui.sixth_yes import open_savings_plan_window
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BG_COLOR
from src.settings.next_button import create_next_button

def open_savings_input_window(previous_window, income, spending_data, user_id, month):
    previous_window.destroy()

    fifth_yes = tk.Tk()
    fifth_yes.title("Savings Goal Input")
    fifth_yes.geometry(f"{WIDTH}x{HEIGHT}")
    fifth_yes.resizable(False, False)
    fifth_yes.configure(bg=BG_COLOR)

    tk.Label(fifth_yes, text="Budget Planner", font=("Arial", 24, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(30, 10))

    tk.Label(fifth_yes, text="Enter amount of\nyour savings goal:", font=("Arial", 14),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(10, 5))

    goal_entry = tk.Entry(fifth_yes, font=("Arial", 13), width=30,
                          highlightbackground=TEXT_COLOR, highlightthickness=1)
    goal_entry.pack(pady=(0, 10))

    tk.Label(fifth_yes, text="Enter in what time you\nwant to achieve this goal (months):",
             font=("Arial", 14), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(10, 5))

    time_entry = tk.Entry(fifth_yes, font=("Arial", 13), width=30,
                          highlightbackground=TEXT_COLOR, highlightthickness=1)
    time_entry.pack(pady=(0, 10))

    error_label = tk.Label(fifth_yes, text="", font=("Arial", 10), fg="red", bg=BG_COLOR)
    error_label.pack()

    def on_next():
        goal = goal_entry.get().strip()
        time = time_entry.get().strip()

        if not goal or not time:
            error_label.config(text="All fields are required.")
            return
        try:
            goal = int(goal)
            time = int(time)
        except ValueError:
            error_label.config(text="Please enter valid numbers only.")
            return

        error_label.config(text="")
        open_savings_plan_window(fifth_yes, goal, time, int(income), spending_data, user_id, month)

    next_button = create_next_button(fifth_yes, on_next)
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    fifth_yes.mainloop()