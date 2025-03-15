import tkinter as tk
from tkinter import ttk
import random

class GeneratePassword:

    def __init__(self, root):
        self.root = root

    def create_password_window(self):
        self.root.geometry("410x200")
        self.root.title("Password Generator")

        self.length_label = ttk.Label(self.root, text="Enter the length of the password:")
        self.length_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)
        self.length_text = tk.StringVar()
        self.length_entry = ttk.Entry(self.root, textvariable=self.length_text)
        self.length_entry.grid(column=1, row=0, sticky="w", padx=5, pady=5)

        self.rep_label = ttk.Label(self.root, text="Repetition? 1: no repetiton, 2: otherwise:")
        self.rep_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
        self.rep_text = tk.StringVar()
        self.rep_text = ttk.Entry(self.root, textvariable=self.rep_text)
        self.rep_text.grid(column=1, row=1, sticky="w", padx=5, pady=5)

        self.generate_btn = ttk.Button(self.root, text="Generate Password", width=20, command=self.generate_password)
        self.generate_btn.grid(column=0, row=2, columnspan=2, sticky="s", padx=10, pady=10)

        self.created_label = ttk.Label(self.root, text="Password Created:")
        self.created_label.grid(column=0, row=3, sticky="w", padx=5, pady=5)
        self.password_text = tk.StringVar()
        self.created_label = ttk.Label(self.root, textvariable=self.password_text)
        self.created_label.grid(column=1, row=3, sticky="w", padx=5, pady=5)

        self.root.mainloop()
        
    def generate_password(self):
        print("password generated!")

    def main(self):
        self.create_password_window()

if __name__ == "__main__":
    window = tk.Tk()
    generate = GeneratePassword(window)
    generate.main()

    