# Graph Algorithms Visualization
==============================

This project demonstrates the visualization of various graph algorithms using Python, Tkinter for GUI, NetworkX for graph operations, and Matplotlib for graph visualization.

## Table of Contents
-----------------

*   [Introduction](#introduction)
*   [Features](#features)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Algorithms Implemented](#algorithms-implemented)
*   [Contributing](#contributing)
*   [License](#license)

## Introduction
------------

Graph Algorithms Visualization is a Python application designed to visually represent the workings of graph algorithms such as Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra's Shortest Path, Minimum Spanning Tree (Kruskal's algorithm), and Strongly Connected Components (Kosaraju's algorithm). It provides an interactive GUI where users can create custom graphs, choose algorithms to apply, and observe how these algorithms traverse or modify the graph.

## Features
--------

*   Create custom graphs with specified number of nodes and edges.
*   Choose between undirected and directed graph types.
*   Select from various layout options like Spring Layout, Circular Layout, Random Layout, and Binary Tree Layout for graph visualization.
*   Perform DFS and BFS traversals with step-by-step visualization.
*   Execute Dijkstra's algorithm to find the shortest path from a specified root node.
*   Compute the Minimum Spanning Tree using Kruskal's algorithm.
*   Find the Strongly Connected Components withing a directed graph using Kosaraju's algorithm.

## Installation
------------

To run the Graph Algorithms Visualization application locally, follow these steps:

1.  **Clone the repository:**
    
    ```bash
    git clone https://github.com/shreyash1110/graph_algo_visualizer.git
    cd graph_algo_visualizer
    ```
    
2.  **Install dependencies:**
    
    Ensure you have Python 3.x installed. Install the required Python libraries using pip:
    
    ```bash
    pip install networkx
    pip install matplotlib
    ```
    
3.  **Run the application:**
    
    Execute the main script to launch the application:
    
    ```bash
    python main.py
    ```

## Usage
-----

Upon launching the application, you will be presented with a graphical interface where you can create graphs, select algorithms, and visualize their operations on the graph. Follow the on-screen instructions to interact with the application.

## Algorithms Implemented
----------------------

The following graph algorithms are implemented in this project:

*   **Depth-First Search (DFS):** Traverse the graph depth-first, highlighting nodes as they are visited.
*   **Breadth-First Search (BFS):** Traverse the graph breadth-first, showing the current level of nodes being processed.
*   **Dijkstra's Shortest Path Algorithm:** Find the shortest path from a specified root node to all other nodes in the graph.
*   **Minimum Spanning Tree (Kruskals's Algorithm):** Compute the Minimum Spanning Tree of the graph.
*   **Strongly Connected Components (Kosaraju's Algorithm):** Finding the Strongly Connected Components in a directed graph.

## Contributing
------------

Contributions to this project are welcome! Here are some ways you can contribute:

*   Implement additional graph algorithms.
*   Improve the GUI design and user experience.
*   Optimize the algorithms for larger graphs.
*   Fix bugs and issues reported by other users.

To contribute, fork the repository, make your changes, and submit a pull request. Please adhere to the code style used in the project and ensure all tests pass before submitting.

## License
-------

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
