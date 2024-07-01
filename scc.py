import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variables for GUI components
num_nodes_entry = None
edges_entry = None
canvas = None
fig = None
ax = None
G = None
node_colors = {}
root = None
scc_list = []
original_graph = None

# Define colors for SCCs globally
colors = ['orange', 'pink', 'green', 'purple', 'cyan', 'magenta', 'brown']

def create_widgets(root):
    global num_nodes_entry, edges_entry, canvas, fig, ax

    input_frame = tk.Frame(root, padx=20, pady=20)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    # First line of input widgets
    num_nodes_label = tk.Label(input_frame, text="Number of Nodes:", font=("Arial", 12))
    num_nodes_label.pack(side=tk.LEFT, padx=10, pady=5)
    num_nodes_entry = tk.Entry(input_frame, font=("Arial", 12))
    num_nodes_entry.pack(side=tk.LEFT, padx=10, pady=5)

    edges_label = tk.Label(input_frame, text="Edges (e.g., 1 2, 2 3):", font=("Arial", 12))
    edges_label.pack(side=tk.LEFT, padx=10, pady=5)
    edges_entry = tk.Entry(input_frame, font=("Arial", 12))
    edges_entry.pack(side=tk.LEFT, padx=10, pady=5)

    # Create buttons
    create_button = tk.Button(input_frame, text="Create Graph", command=create_graph, font=("Arial", 12))
    create_button.pack(side=tk.LEFT, padx=10, pady=10)

    scc_button = tk.Button(input_frame, text="Find SCC", command=find_scc, font=("Arial", 12))
    scc_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Create canvas for matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust figure size
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

def create_graph():
    global G, original_graph

    G = nx.DiGraph()
    edge_list = [tuple(map(int, edge.strip().split())) for edge in edges_entry.get().split(',')]
    G.add_edges_from(edge_list)

    original_graph = G.copy()  # Store a copy of the original graph for display purposes
    draw_graph()

def draw_graph():
    global G, ax, canvas, node_colors

    ax.clear()
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color=[node_colors.get(node, 'blue') for node in G.nodes()], node_size=700, font_size=12, font_color='white', font_weight='bold', ax=ax)
    canvas.draw()

def find_scc():
    global G, node_colors, scc_list

    scc_list = list(nx.kosaraju_strongly_connected_components(G))
    color_scc()

def color_scc():
    global G, node_colors, scc_list

    for scc_index, scc in enumerate(scc_list):
        for node in scc:
            node_colors[node] = colors[scc_index % len(colors)]
            animate_coloring()
    

def animate_coloring():
    global G, ax, canvas, node_colors, original_graph

    # Restore the original graph for animation
    G = original_graph.copy()

    # Animate coloring based on Kosaraju's algorithm
    for scc_index, scc in enumerate(scc_list):
        color = colors[scc_index % len(colors)]
        for node in scc:
            node_colors[node] = color
        draw_graph()
        canvas.get_tk_widget().update()
        canvas.get_tk_widget().after(1000)  # Adjust delay as needed (in milliseconds)

def main():
    global root
    root = tk.Tk()
    root.title("Kosaraju's Algorithm Visualization for SCC")
    root.geometry("800x600")
    create_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()
