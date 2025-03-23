import tkinter as tk

WIDTH = 375
HEIGHT = 645
TEXT_COLOR = "#0B2447"
BUTTON_BG = "#FFFFFF"
BUTTON_HIGHLIGHT = "#0B2447"
BG_COLOR = "#E7E7E6"
EURO_IMAGE_PATH = "photos/euro_photo.png" 

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

    tk.Label(input_frame, text="User ID", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    user_id_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2, highlightbackground=TEXT_COLOR, highlightthickness=1)
    user_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Month", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    month_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2, highlightbackground=TEXT_COLOR, highlightthickness=1)
    month_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Monthly Income", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    income_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2, highlightbackground=TEXT_COLOR, highlightthickness=1)
    income_entry.grid(row=2, column=1, padx=10, pady=5)

    euro_img = tk.PhotoImage(file=EURO_IMAGE_PATH)
    euro_label = tk.Label(second, image=euro_img, bg=BG_COLOR)
    euro_label.image = euro_img  
    euro_label.pack(pady=30)

    next_button = tk.Button(
        second,
        text="Next →",
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        activebackground="#DADADA",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Next log…") 
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
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    command=open_second_window
)
enter_button.place(relx=0.5, rely=0.50, anchor="center")

root.mainloop()
