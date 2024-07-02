import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import subprocess

def main_menu():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Prompt user to choose an option
    choice = simpledialog.askstring("Algorithm Choice", "Choose an algorithm:\n1. Traversal\n2. Shortest Path (Dijkstra)\n3. Strongly Connected Components (Kosaraju)\n4. Minimum Spanning Tree (Prim)")

    if choice == "1":
        messagebox.showinfo("Choice", "You chose Traversal.")
        run_traversal_algorithm()
    elif choice == "2":
        messagebox.showinfo("Choice", "You chose Shortest Path (Dijkstra).")
        run_dijkstra_algorithm()
    elif choice == "3":
        messagebox.showinfo("Choice", "You chose Strongly Connected Components (Kosaraju).")
        run_scc_algorithm()
    elif choice == "4":
        messagebox.showinfo("Choice", "You chose Minimum Spanning Tree (Kruskals).")
        run_mst_algorithm()
    else:
        messagebox.showerror("Error", "Invalid choice. Please select 1, 2, 3, or 4.")

def run_traversal_algorithm():
    try:
        # Execute traversal.py using subprocess
        subprocess.run(["python", "traversal.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing traversal.py: {e}")

def run_dijkstra_algorithm():
    try:
        # Execute shortest_path.py using subprocess
        subprocess.run(["python", "shortest_path.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing shortest_path.py: {e}")

def run_scc_algorithm():
    try:
        # Execute scc.py using subprocess
        subprocess.run(["python", "scc.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing SCC algorithm: {e}")

def run_mst_algorithm():
    try:
        # Execute mst.py using subprocess 
        subprocess.run(["python", "kruskals.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error executing MST algorithm: {e}")

if __name__ == "__main__":
    main_menu()
