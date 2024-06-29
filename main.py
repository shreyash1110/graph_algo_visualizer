import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import subprocess

def main_menu():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Prompt user to choose an option
    choice = simpledialog.askstring("Algorithm Choice", "Choose an algorithm:\n1. Traversal\n2. Shortest Path (Dijkstra)")

    if choice == "1":
        messagebox.showinfo("Choice", "You chose Traversal.")
        run_traversal_algorithm()
    elif choice == "2":
        messagebox.showinfo("Choice", "You chose Shortest Path (Dijkstra).")
        run_dijkstra_algorithm()
    else:
        messagebox.showerror("Error", "Invalid choice. Please select 1 or 2.")

def run_traversal_algorithm():
    try:
        # Execute traversal.py using subprocess
        subprocess.run(["python", "project\traversal.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing traversal.py: {e}")

def run_dijkstra_algorithm():
    try:
        subprocess.run(["python", "project\shortest_path.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing shortest_path.py: {e}")

if __name__ == "__main__":
    main_menu()
