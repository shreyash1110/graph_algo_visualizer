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
mst_edges = []
edge_index = 0

def create_widgets(root):
    global num_nodes_entry, edges_entry, canvas, fig, ax

    input_frame = tk.Frame(root, padx=20, pady=20)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    # First line of input widgets
    num_nodes_label = tk.Label(input_frame, text="Number of Nodes:", font=("Arial", 12))
    num_nodes_label.pack(side=tk.LEFT, padx=10, pady=5)
    num_nodes_entry = tk.Entry(input_frame, font=("Arial", 12))
    num_nodes_entry.pack(side=tk.LEFT, padx=10, pady=5)

    edges_label = tk.Label(input_frame, text="Edges (e.g., 1 2 5, 2 3 3):", font=("Arial", 12))
    edges_label.pack(side=tk.LEFT, padx=10, pady=5)
    edges_entry = tk.Entry(input_frame, font=("Arial", 12))
    edges_entry.pack(side=tk.LEFT, padx=10, pady=5)

    # Create buttons
    create_button = tk.Button(input_frame, text="Create Graph", command=create_graph, font=("Arial", 12))
    create_button.pack(side=tk.LEFT, padx=10, pady=10)

    mst_button = tk.Button(input_frame, text="Find MST", command=get_graph_input, font=("Arial", 12))
    mst_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Create canvas for matplotlib
    fig, ax = plt.subplots(figsize=(12, 9))  # Adjust figure size for fullscreen appearance
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

def create_graph():
    global G
    G = nx.Graph()
    

def get_graph_input():
    global mst_edges, edge_index
    try:
        create_graph()  # Ensure the graph is created before processing
        num = int(num_nodes_entry.get())
        edge_list = [tuple(map(int, edge.strip().split())) for edge in edges_entry.get().split(',')]
        validate_input(num, edge_list)
        mst_edges = kruskal(num, edge_list)
        edge_index = 0
        root.after(2000, animate_mst)
    except ValueError:
        print("Invalid input format. Please enter the number of nodes and edges correctly.")
    except IndexError as e:
        print(f"Error: {e}")

def validate_input(num, edge_list):
    for u, v, w in edge_list:
        if u > num or v > num or u <= 0 or v <= 0:
            raise IndexError(f"Node indices must be between 1 and {num}")

# Kruskal's algorithm
def kruskal(num, edge_list):
    
    parent = list(range(num + 1))
    rank = [0] * (num + 1)

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    edge_list.sort(key=lambda x: x[2])  # Sort edges by weight

    for u, v, weight in edge_list:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst

def update_graph(edge):
    global G, ax, canvas, node_colors
    u, v, weight = edge
    G.add_edge(u, v, weight=weight)
    
    # Assign colors to the connected components
    components = list(nx.connected_components(G))
    color_map = {}
    for idx, component in enumerate(components):
        color = f'C{idx % 10}'  # Cycle through 10 different colors
        for node in component:
            color_map[node] = color
            node_colors[node] = color
    
    pos = nx.spring_layout(G)
    ax.clear()
    node_list = G.nodes()
    colors = [color_map[node] for node in node_list]
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=700, font_size=10, font_weight="bold", ax=ax)
    edge_labels = {(u, v): str(G[u][v]['weight']) for u, v in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)
    canvas.draw()

def animate_mst():
    global edge_index
    if edge_index < len(mst_edges):
        update_graph(mst_edges[edge_index])
        edge_index += 1
        root.after(2000, animate_mst)

def main():
    global root
    root = tk.Tk()
    root.title("Graph Input for MST")
    create_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()
