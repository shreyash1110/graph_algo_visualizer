import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variables for GUI components and graph data
num_nodes_entry = None
edges_entry = None
root_node_entry = None
canvas = None
figure = None
ax = None

def create_widgets(root):
    global num_nodes_entry, edges_entry, root_node_entry, canvas, figure, ax

    input_frame = tk.Frame(root)
    input_frame.pack(padx=20, pady=20)

    # First line of input widgets
    num_nodes_label = tk.Label(input_frame, text="Number of Nodes:", font=("Arial", 12))
    num_nodes_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    num_nodes_entry = tk.Entry(input_frame)
    num_nodes_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    edges_label = tk.Label(input_frame, text="Edges (e.g., 1 2 5, 2 3 3):", font=("Arial", 12))
    edges_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    edges_entry = tk.Entry(input_frame)
    edges_entry.grid(row=0, column=3, padx=10, pady=5, sticky="w")

    root_node_label = tk.Label(input_frame, text="Root Node for Shortest Paths:", font=("Arial", 12))
    root_node_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")
    root_node_entry = tk.Entry(input_frame)
    root_node_entry.grid(row=0, column=5, padx=10, pady=5, sticky="w")

    # Create buttons
    create_button = tk.Button(input_frame, text="Create Graph", command=create_graph)
    create_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    dijkstra_button = tk.Button(input_frame, text="Start Algorithm", command=get_graph_input)
    dijkstra_button.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Canvas for displaying graphs
    figure = plt.Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.get_tk_widget().pack(padx=20, pady=20)

def create_graph():
    num_nodes = int(num_nodes_entry.get())
    edges = [tuple(map(int, edge.strip().split())) for edge in edges_entry.get().split(',')]

    G = nx.Graph()
    G.add_nodes_from(range(1, num_nodes + 1))
    G.add_weighted_edges_from(edges)

    draw_graph(G)

def get_graph_input():
    num = int(num_nodes_entry.get())
    edge_list = [tuple(map(int, edge.strip().split())) for edge in edges_entry.get().split(',')]
    root = int(root_node_entry.get())
    final_directed_graph = dijkstra(num, edge_list, root)
    visualize_graph(final_directed_graph)

# Dijkstra's algorithm
def dijkstra(num, edge_list, root):
    graph = [[] for _ in range(num + 1)]
    for u, v, w in edge_list:
        graph[u].append([v, w])
        graph[v].append([u, w])

    import heapq
    pq = []
    heapq.heappush(pq, (0, root))  # Push the root node with distance 0
    dist = [float('inf')] * (num + 1)
    dist[root] = 0
    visited = [False] * (num + 1)
    parent = [[] for _ in range(num + 1)]

    while pq:
        curr_dist, curr = heapq.heappop(pq)
        if visited[curr]:
            continue
        visited[curr] = True
        for neighbor, weight in graph[curr]:
            if visited[neighbor] and dist[neighbor] == dist[curr] + weight:
                parent[neighbor].append([curr, weight])
                continue
            if not visited[neighbor] and dist[neighbor] > dist[curr] + weight:
                if parent[neighbor]:
                    parent[neighbor].pop()
                parent[neighbor].append([curr, weight])
                dist[neighbor] = dist[curr] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    final_directed_graph = []
    for i in range(1, num + 1):
        for j in parent[i]:
            final_directed_graph.append([j[0],i,j[1]])

    return final_directed_graph

def draw_graph(G):
    global ax, canvas
    ax.clear()
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="orange", font_size=10, font_weight="bold", ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)
    canvas.draw()

def visualize_graph(graph):
    global ax, canvas
    ax.clear()
    G = nx.DiGraph()
    for u, v, weight in graph:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): str(weight) for u, v, weight in graph}

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="orange", font_size=10, font_weight="bold", arrows=True, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=ax)
    canvas.draw()

def main():
    root = tk.Tk()
    root.title("Graph Input")
    create_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()
