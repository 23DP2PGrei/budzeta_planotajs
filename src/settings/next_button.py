import tkinter as tk
from src.settings.parameters import TEXT_COLOR, BG_COLOR

def create_next_button(window, command):
    return tk.Button(
        window,
        text="Next →", # Pogas teksts
        font=("Arial", 12, "bold"), # Fonts un stils
        fg=TEXT_COLOR, # Teksta krāsa
        bg=BG_COLOR, # Fona krāsa
        activebackground="#DADADA", # Fona krāsa, kad poga ir aktīva
        bd=0, # Bez apmales
        highlightthickness=0, # Bez ārējās apmales
        command=command # Funkcija, ko izpilda, kad spiež
    )