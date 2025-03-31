import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

WIDTH = 375
HEIGHT = 645
TEXT_COLOR = "#0B2447"
BUTTON_BG = "#FFFFFF"
BUTTON_HIGHLIGHT = "#0B2447"
BG_COLOR = "#E7E7E6"
EURO_IMAGE_PATH = "photos/euro_photo.png" 

def open_results_window(previous_window, income, spending_data):
    previous_window.destroy()

    total_spent = sum(spending_data.values())
    income = int(income)
    balance = income - total_spent

    fig, ax = plt.subplots(figsize=(3.2, 3.2), dpi=100)

    categories = list(spending_data.keys())
    values = list(spending_data.values())

    wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    startangle=90,
    textprops={'fontsize': 8, 'color': TEXT_COLOR},
    autopct='%1.1f%%'
    )

    ax.axis('equal')

    ax.text(0, 0, f"{sum(values)}€", ha='center', va='center',
        fontsize=16, fontweight='bold', color=TEXT_COLOR)

    fifth = tk.Tk()
    fifth.title("Budget Summary")
    fifth.geometry(f"{WIDTH}x{HEIGHT}")
    fifth.resizable(False, False)
    fifth.configure(bg=BG_COLOR)

    tk.Label(fifth, text="Budget Planner", font=("Arial", 24, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(20, 5))

    canvas = FigureCanvasTkAgg(fig, master=fifth)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    balance_text = f"Balance: {balance}€"
    tk.Label(fifth, text=balance_text, font=("Arial", 14),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(10, 5))

    done_button = tk.Button(
        fifth,
        text="Done", 
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        activebackground="#DADADA",
        bd=0,
        highlightthickness=0,
        command=fifth.destroy
        )
    done_button.place(relx=0.95, rely=0.97, anchor="se")

    fifth.mainloop()

def open_savings_goal_window(previous_window, income, spending_data):
    previous_window.destroy()

    fourth = tk.Tk()
    fourth.title("Savings Goal")
    fourth.geometry(f"{WIDTH}x{HEIGHT}")
    fourth.resizable(False, False)
    fourth.configure(bg=BG_COLOR)

    tk.Label(fourth, text="Budget Planner", font=("Arial", 24, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(30, 10))

    tk.Label(fourth, text="Do you have\na savings goal?",
             font=("Arial", 18, "bold"),
             fg=TEXT_COLOR, bg=BG_COLOR, justify="center").pack(pady=(20, 20))

    button_frame = tk.Frame(fourth, bg=BG_COLOR)
    button_frame.pack()

    def on_yes():
        print("User selected YES")

    def on_no():
        open_results_window(fourth, income, spending_data)
      
    yes_button = tk.Button(button_frame, text="Yes", font=("Arial", 14),
                           bg=BUTTON_BG, fg=TEXT_COLOR, bd=1, width=8, command=on_yes)
    yes_button.grid(row=0, column=0, padx=10)

    no_button = tk.Button(button_frame, text="No", font=("Arial", 14),
                          bg=BUTTON_BG, fg=TEXT_COLOR, bd=1, width=8, command=on_no)
    no_button.grid(row=0, column=1, padx=10)

    fourth.mainloop()

def open_third_window(previous_window, income):
    previous_window.destroy()

    third = tk.Tk()
    third.title("Enter Spending")
    third.geometry(f"{WIDTH}x{HEIGHT}")
    third.resizable(False, False)
    third.configure(bg=BG_COLOR)

    tk.Label(third, text="Budget Planner", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(20, 5))
    tk.Label(third, text="Enter Spending:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", padx=20)

    content_frame = tk.Frame(third, bg=BG_COLOR)
    content_frame.pack(pady=10)

    category_entries = []
    base_font_size = 13

    def update_fonts():
        nonlocal base_font_size
        if len(category_entries) > 5:
            base_font_size = max(13, 13 - (len(category_entries) // 2))
        for label, entry in category_entries:
            label.config(font=("Arial", base_font_size))
            entry.config(font=("Arial", base_font_size))

    def add_category(name):
        row = len(category_entries)
        label = tk.Label(content_frame, text=name, font=("Arial", base_font_size),
                         bg=BG_COLOR, fg=TEXT_COLOR, anchor="w")
        label.grid(row=row, column=0, sticky="w", padx=(20, 10), pady=5)

        entry = tk.Entry(content_frame, font=("Arial", base_font_size),
                         width=18, bd=2, highlightbackground=TEXT_COLOR, highlightthickness=1)
        entry.grid(row=row, column=1, sticky="e", padx=(5, 20), pady=5)

        category_entries.append((label, entry))
        update_fonts()

    for cat in ["Food", "Healthcare", "Rent", "Loans"]:
        add_category(cat)

    add_frame = tk.Frame(third, bg=BG_COLOR)
    add_frame.pack(pady=(15, 0), anchor="w", padx=20)

    add_button = tk.Button(add_frame, text="Add", font=("Arial", 12),
                           bg=BUTTON_BG, fg=TEXT_COLOR, bd=1)
    add_button.grid(row=0, column=0, sticky="w")

    def show_category_input():
        add_button.grid_remove()

        input_frame = tk.Frame(third, bg=BG_COLOR)
        input_frame.pack(pady=(10, 0), anchor="w", padx=20)

        prompt = tk.Label(input_frame, text="Enter category name:", font=("Arial", 12),
                          bg=BG_COLOR, fg=TEXT_COLOR)
        prompt.grid(row=0, column=0, sticky="w", pady=5)

        cat_entry = tk.Entry(input_frame, font=("Arial", 12),
                             highlightbackground=TEXT_COLOR, highlightthickness=1)
        cat_entry.grid(row=1, column=0, sticky="w", pady=5)

        def confirm_add():
            category_name = cat_entry.get().strip()
            if category_name:
                input_frame.destroy()
                add_category(category_name)
                if len(category_entries) < 10:
                    add_button.grid(row=0, column=0, sticky="w")

        confirm_button = tk.Button(input_frame, text="Confirm", font=("Arial", 11),
                                   command=confirm_add, bg=BUTTON_BG, fg=TEXT_COLOR)
        confirm_button.grid(row=2, column=0, sticky="w", pady=5)

    add_button.config(command=show_category_input)

    error_label = tk.Label(third, text="", font=("Arial", 10), fg="red", bg=BG_COLOR)
    error_label.pack()

    def get_spending_data():
        data = {}
        for label, entry in category_entries:
            name = label.cget("text")
            try:
                amount = int(entry.get())
            except ValueError:
                amount = 0
            data[name] = amount
        return data


    def validate_and_continue():
        for label, entry in category_entries:
            if not entry.get().strip():
                error_label.config(text="Please fill in all fields.")
                return
        spending_data = get_spending_data()
        open_savings_goal_window(third, income, spending_data)

    next_button = tk.Button(
        third,
        text="Next →",
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        activebackground="#DADADA",
        bd=0,
        highlightthickness=0,
        command=validate_and_continue
    )
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    third.mainloop()

def open_second_window():
    root.destroy()

    second = tk.Tk()
    second.title("Enter Data")
    second.geometry(f"{WIDTH}x{HEIGHT}")
    second.resizable(False, False)
    second.configure(bg=BG_COLOR)

    title = tk.Label(
        second,
        text="Budget Planner",
        font=("Arial", 24, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    title.pack(pady=(30, 10))

    label_data = tk.Label(
        second,
        text="Enter Data:",
        font=("Arial", 16, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    label_data.pack(pady=(0, 10))

    input_frame = tk.Frame(second, bg=BG_COLOR)
    input_frame.pack()

    tk.Label(input_frame, text="User ID", font=("Arial", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    user_id_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2,
                             highlightbackground=TEXT_COLOR, highlightthickness=1)
    user_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Month", font=("Arial", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    selected_month = tk.StringVar()
    selected_month.set("Select Month")  # default
    month_menu = tk.OptionMenu(input_frame, selected_month, *months)
    month_menu.config(font=("Arial", 11), bg=BUTTON_BG, fg=TEXT_COLOR, highlightthickness=1,
                      highlightbackground=TEXT_COLOR)
    month_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(input_frame, text="Monthly Income", font=("Arial", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    income_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2,
                            highlightbackground=TEXT_COLOR, highlightthickness=1)
    income_entry.grid(row=2, column=1, padx=10, pady=5)

    error_label = tk.Label(second, text="", font=("Arial", 10),
                           fg="red", bg=BG_COLOR)
    error_label.pack()

    euro_img = tk.PhotoImage(file=EURO_IMAGE_PATH)
    euro_label = tk.Label(second, image=euro_img, bg=BG_COLOR)
    euro_label.image = euro_img
    euro_label.pack(pady=30)

    def validate_and_continue():
        user_id = user_id_entry.get().strip()
        month = selected_month.get()
        income_str = income_entry.get().strip()

        if not user_id or month == "Select Month" or not income_str:
            error_label.config(text="Please fill in all fields.")
            return

        try:
            int(income_str)
        except ValueError:
            error_label.config(text="Monthly income must be a number.")
            return

        error_label.config(text="")
        open_third_window(second, income_str)

    next_button = tk.Button(
        second,
        text="Next →",
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        activebackground="#DADADA",
        bd=0,
        highlightthickness=0,
        command=validate_and_continue
    )
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    second.mainloop()

root = tk.Tk()
root.title("Budget Planner")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

title = tk.Label(
    root,
    text="Budget Planner",
    font=("Arial", 28, "bold"),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
title.place(relx=0.5, rely=0.35, anchor="center")

enter_button = tk.Button(
    root, 
    text="Enter", 
    activebackground=BUTTON_HIGHLIGHT, 
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="white",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 16),
    height=1,
    width=12,
    justify="center",
    overrelief="raised",
    command=open_second_window
)
enter_button.place(relx=0.5, rely=0.50, anchor="center")

root.mainloop()
