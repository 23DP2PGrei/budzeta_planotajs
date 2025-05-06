import tkinter as tk
from src.ui.third import open_third_window
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BUTTON_BG, BG_COLOR, EURO_IMAGE_PATH
from src.settings.next_button import create_next_button

def open_second_window(previous_window):
    previous_window.destroy()

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
    selected_month.set("Select Month")
    month_menu = tk.OptionMenu(input_frame, selected_month, *months)
    month_menu.config(font=("Arial", 11), bg=BUTTON_BG, fg=TEXT_COLOR,
                      highlightthickness=1, highlightbackground=TEXT_COLOR)
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
        open_third_window(second, income_str, user_id, month)

    next_button = create_next_button(second, validate_and_continue)
    next_button.place(relx=0.95, rely=0.97, anchor="se")

    second.mainloop()