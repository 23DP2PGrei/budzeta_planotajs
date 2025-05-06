import tkinter as tk
from src.ui.second import open_second_window
from src.settings.parameters import WIDTH, HEIGHT, TEXT_COLOR, BUTTON_HIGHLIGHT, BG_COLOR, BUTTON_BG

def start_app():
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
        bg=BUTTON_BG,
        disabledforeground="gray",
        fg="black",
        font=("Arial", 16),
        height=1,
        width=12,
        justify="center",
        overrelief="raised",
        command=lambda: open_second_window(root)
    )
    enter_button.place(relx=0.5, rely=0.50, anchor="center")

    root.mainloop()