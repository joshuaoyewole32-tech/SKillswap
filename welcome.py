import tkinter as tk
from tkinter import ttk

class WelcomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to SKillswap Repository")
        self.geometry("500x300")
        self.configure(bg="#f5f5f5")
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="Welcome to SKillswap!", font=("Helvetica", 20, "bold"), background="#f5f5f5")
        title.pack(pady=30)

        desc = ttk.Label(self, text="This repository is dedicated to skill sharing and collaboration.\nExplore, contribute, and grow your skills!", font=("Helvetica", 12), background="#f5f5f5")
        desc.pack(pady=10)

        btn = ttk.Button(self, text="Get Started", command=self.on_get_started)
        btn.pack(pady=20)

    def on_get_started(self):
        tk.messagebox.showinfo("Get Started", "Thank you for your interest! Explore the repository to learn more.")

if __name__ == "__main__":
    app = WelcomePage()
    app.mainloop()
