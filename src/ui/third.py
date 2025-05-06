import tkinter as tk
from src.settings.apreikins import get_spending_data
from src.ui.fourth import open_savings_goal_window
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BUTTON_BG, BG_COLOR
from src.settings.next_button import create_next_button

def open_third_window(previous_window, income, user_id, month):
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

    def validate_and_continue():
        for label, entry in category_entries:
            if not entry.get().strip():
                error_label.config(text="Please fill in all fields.")
                return
        spending_data = get_spending_data(category_entries)
        open_savings_goal_window(third, income, spending_data, user_id, month)

    next_button = create_next_button(third, validate_and_continue)
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    third.mainloop()