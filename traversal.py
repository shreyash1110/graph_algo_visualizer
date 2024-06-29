import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from threading import Thread

# Global variables for GUI components and graph
num_nodes_entry = None
edges_entry = None
root_node_entry = None
G = None
pos = None
node_colors = None
current_node = None
canvas = None
fig = None
ax = None
visited = None
operation_var = None
layout_var = None

def create_widgets(root):
    global num_nodes_entry, edges_entry, root_node_entry, operation_var, layout_var

    input_frame = tk.Frame(root)
    input_frame.pack(padx=20, pady=20)

    # First line of input widgets
    num_nodes_label = tk.Label(input_frame, text="Number of Nodes:", font=("Arial", 12))
    num_nodes_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    num_nodes_entry = tk.Entry(input_frame)
    num_nodes_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    operation_var = tk.StringVar(root)
    operation_var.set("Undirected Graph")
    operation_label = tk.Label(input_frame, text="Graph Type:", font=("Arial", 12))
    operation_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    operation_menu = tk.OptionMenu(input_frame, operation_var, "Undirected Graph", "Directed Graph")
    operation_menu.grid(row=0, column=3, padx=10, pady=5, sticky="w")

    edges_label = tk.Label(input_frame, text="Edges (e.g., 1 2, 2 3):", font=("Arial", 12))
    edges_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    edges_entry = tk.Entry(input_frame)
    edges_entry.grid(row=0, column=5, padx=10, pady=5, sticky="w")

    root_node_label = tk.Label(input_frame, text="Root Node for Traversal:", font=("Arial", 12))
    root_node_label.grid(row=0, column=6, padx=10, pady=5, sticky="w")
    root_node_entry = tk.Entry(input_frame)
    root_node_entry.grid(row=0, column=7, padx=10, pady=5, sticky="w")

    # Second line of input widgets
    create_button = tk.Button(input_frame, text="Create Graph", command=create_graph)
    create_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    traversal_label = tk.Label(input_frame, text="Choose Traversal:", font=("Arial", 12))
    traversal_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    dfs_button = tk.Button(input_frame, text="Perform DFS", command=perform_dfs)
    dfs_button.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    bfs_button = tk.Button(input_frame, text="Perform BFS", command=perform_bfs)
    bfs_button.grid(row=1, column=3, padx=10, pady=5, sticky="w")

    # Layout options
    layout_var = tk.StringVar(root)
    layout_var.set("Spring Layout")
    layout_label = tk.Label(input_frame, text="Graph Layout:", font=("Arial", 12))
    layout_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")
    layout_menu = tk.OptionMenu(input_frame, layout_var, "Spring Layout", "Circular Layout", "Random Layout", "Binary Tree Layout")
    layout_menu.grid(row=1, column=5, padx=10, pady=5, sticky="w")

def create_canvas(root):
    global fig, ax, canvas

    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def create_graph():
    global G, pos, node_colors, visited

    # Resetting graph and traversal state
    G = None
    pos = None
    node_colors = None
    visited = None
    ax.clear()
    canvas.draw()

    num_nodes = int(num_nodes_entry.get())
    edges_input = edges_entry.get()
    edges_list = edges_input.split(',')
    edges = [tuple(map(int, edge.strip().split())) for edge in edges_list]

    graph_type = operation_var.get()

    if graph_type == "Undirected Graph":
        G = nx.Graph()
        G.add_nodes_from(range(1, num_nodes + 1))
        G.add_edges_from(edges)
    elif graph_type == "Directed Graph":
        G = nx.DiGraph()
        G.add_nodes_from(range(1, num_nodes + 1))
        G.add_edges_from(edges)

    pos = get_graph_layout(G)
    node_colors = ['orange'] * (num_nodes + 1)
    update_graph()

def get_graph_layout(graph):
    layout_type = layout_var.get()

    if layout_type == "Spring Layout":
        return nx.spring_layout(graph)
    elif layout_type == "Circular Layout":
        return nx.circular_layout(graph)
    elif layout_type == "Random Layout":
        return nx.random_layout(graph)
    elif layout_type == "Binary Tree Layout":
        return nx.balanced_tree(2, 5)  # Adjust parameters as needed for binary tree layout

def update_graph():
    ax.clear()
    if isinstance(G, nx.DiGraph):
        nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=node_colors[1:], edge_color='#000000', node_size=800, font_size=12, arrows=True)
    else:
        nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=node_colors[1:], edge_color='#000000', node_size=800, font_size=12)

    # Draw the current node with a black ring
    if current_node is not None:
        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='pink', node_size=900, edgecolors='black', linewidths=2)

    canvas.draw()

def perform_dfs():
    global visited
    root_node = int(root_node_entry.get())
    if root_node not in G.nodes:
        print(f"Root node {root_node} is not in the graph.")
        return
    visited = set()
    dfs_thread = Thread(target=dfs, args=(root_node,))
    dfs_thread.start()

def perform_bfs():
    global visited
    root_node = int(root_node_entry.get())
    if root_node not in G.nodes:
        print(f"Root node {root_node} is not in the graph.")
        return
    visited = set()
    bfs_thread = Thread(target=bfs, args=(root_node,))
    bfs_thread.start()

def dfs(node):
    global current_node
    current_node = node
    node_colors[node] = 'pink'
    update_graph()
    time.sleep(0.5)  # Adjusted speed to 0.5 seconds per step

    visited.add(node)
    for neighbor in sorted(G.neighbors(node)):
        if neighbor not in visited:
            node_colors[neighbor] = 'orange'  # Reset edge color
            dfs(neighbor)
            current_node = node
            node_colors[node] = 'pink'
            update_graph()
            time.sleep(0.5)

    current_node = None
    node_colors[node] = 'red'
    update_graph()
    time.sleep(0.5)

def update_bfs_graph(current_nodes):
    ax.clear()
    
    # Draw nodes and edges
    if isinstance(G, nx.DiGraph):
        nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=node_colors[1:], edge_color='#000000', node_size=800, font_size=12, arrows=True)
    else:
        nx.draw(G, pos=pos, ax=ax, with_labels=True, node_color=node_colors[1:], edge_color='#000000', node_size=800, font_size=12)

    # Draw current node with a black ring
    for current_node in current_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='pink', node_size=900, edgecolors='black', linewidths=2)

    canvas.draw()

def bfs(node):
    global current_node
    queue = [node]
    visited.add(node)

    while queue:
        level_nodes = []
        
        # Process nodes at the current level
        while queue:
            current_node = queue.pop(0)
            level_nodes.append(current_node)
            node_colors[current_node] = 'pink'  # Nodes being processed are pink with black edges

        update_bfs_graph(level_nodes)  # Update graph with nodes at current level
        time.sleep(0.5)

        # Process neighbors of nodes at the current level
        for n in level_nodes:
            for neighbor in sorted(G.neighbors(n)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # Mark all nodes at the current level as red
        for n in level_nodes:
            node_colors[n] = 'red'
        level_nodes.clear()
        update_bfs_graph(level_nodes)  # Update graph with nodes marked red
        time.sleep(0.5)

    current_node = None
    update_bfs_graph(list())  # Final update after BFS traversal completes
    time.sleep(0.5)


def main():
    root = tk.Tk()
    root.title("Graph Visualization")
    create_widgets(root)
    create_canvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()