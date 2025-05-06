import tkinter as tk
from src.settings.parameters import TEXT_COLOR, BG_COLOR

def create_next_button(window, command):
    return tk.Button(
        window,
        text="Next →",
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        activebackground="#DADADA",
        bd=0,
        highlightthickness=0,
        command=command
    )