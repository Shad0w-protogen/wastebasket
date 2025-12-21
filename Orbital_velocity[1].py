
from math import sqrt as a
import tkinter as tk
from tkinter import messagebox

def orbitalspeed():
    try:
        radius = float(entry.get())
        if radius <= 0:
            raise ValueError
        v = a(9.82 * radius)
        result_label.config(text=f"Orbital velocity is {v:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Incorrect input: please enter a positive number")

root = tk.Tk()
root.title("Orbital Velocity Calculator")

tk.Label(root, text="Insert radius:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=orbitalspeed)
calc_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
