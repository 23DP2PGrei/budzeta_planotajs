import tkinter as tk
from tkinter import messagebox

def open_expense_window():
    user_window.destroy()  

def open_user_input_window():
    root.destroy() 

    global user_window
    user_window = tk.Tk()
    user_window.title("User Information")
    user_window.geometry("900x500")
    user_window.configure(bg="#7a6a5d")  

    frame = tk.Frame(user_window, bg="#7a6a5d")
    frame.pack(pady=50)

    tk.Label(frame, text="User ID", font=("Arial", 18, "bold"), bg="#7a6a5d", fg="black").grid(row=0, column=0, sticky="w", pady=10, padx=20)
    user_id_entry = tk.Entry(frame, font=("Arial", 18), bg="#d9d9d9", width=20)
    user_id_entry.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Month", font=("Arial", 18, "bold"), bg="#7a6a5d", fg="black").grid(row=1, column=0, sticky="w", pady=10, padx=20)
    month_entry = tk.Entry(frame, font=("Arial", 18), bg="#d9d9d9", width=20)
    month_entry.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Monthly income", font=("Arial", 18, "bold"), bg="#7a6a5d", fg="black").grid(row=2, column=0, sticky="w", pady=10, padx=20)
    income_entry = tk.Entry(frame, font=("Arial", 18), bg="#d9d9d9", width=20)
    income_entry.grid(row=2, column=1, pady=10)

    def validate_and_continue():
        if not user_id_entry.get() or not month_entry.get() or not income_entry.get():
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return
        open_expense_window()

    next_button = tk.Button(user_window, text="Next", font=("Arial", 16, "bold"), bg="#5a4d44", fg="black", width=10, height=1, command=validate_and_continue)
    next_button.place(relx=0.9, rely=0.9, anchor="se") 

    user_window.mainloop()

root = tk.Tk()
root.title("Budget Planner")
root.geometry("900x500")
root.configure(bg="#7a6a5d")

title_label = tk.Label(root, text="Budget Planner", font=("Arial", 32, "bold"), bg="#7a6a5d", fg="black")
title_label.pack(pady=100)

enter_button = tk.Button(root, text="Enter", font=("Arial", 20, "bold"), bg="#5a4d44", fg="black", width=10, height=1, command=open_user_input_window)
enter_button.pack()

root.mainloop()
