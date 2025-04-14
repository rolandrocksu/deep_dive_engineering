from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


class KDTree:

    def __init__(self, value: Point = Point(5, 7), left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"KDTree self.value={self.value} self.left={self.left} self.right={self.right}"


    def insert(self, new_point: Point):
        level = 0
        current_node = self
        print("\n"*3, current_node)
        while True:
            level += 1
            if level % 2:
                if current_node.value.x >= new_point.x:
                    if self.right:
                        current_node = current_node.right
                        continue
                    current_node.right = KDTree(new_point)
                    break
                else:
                    if current_node.left:
                        current_node = current_node.left
                        continue
                    current_node.left = KDTree(new_point)
                    break
            else:
                if current_node.value.y >= new_point.y:
                    if current_node.right:
                        current_node = current_node.right
                        continue
                    current_node.right = KDTree(new_point)
                    break
                else:
                    if current_node.left:
                        current_node = current_node.left
                        continue
                    current_node.left = KDTree(new_point)
                    break

            

    def search_nn(self, query_point: Point):
        pass


if __name__ == "__main__":
    tree = KDTree()

    for item in zip(range(5, 10), range(15, 20)):
        point = Point(*item)
        tree.insert(point)


import networkx as nx
import matplotlib.pyplot as plt


def add_edges(graph, root, parent=None, pos=None, level = 0, x: float = 0.0, dx: float = 1.0):
    pos = pos or {}
    if root is not None:
        pos[root.value] = (x, -level)
        if parent is not None:
            graph.add_edge(parent.value, root.value)
        add_edges(graph, root.left, root, pos, level + 1, x - dx, dx / 2)
        add_edges(graph, root.right, root, pos, level + 1, x + dx, dx / 2)
    return pos


def networkx_graph(root):
    graph = nx.DiGraph()
    positions = add_edges(graph, root)
    # Draw the graph
    plt.figure(figsize=(10, 6))
    nx.draw(graph, positions, with_labels=True, node_size=2000, node_color="skyblue", font_size=14, font_weight="bold",
            arrowsize=20)
    plt.title("Binary Search Tree Visualization")
    plt.show()

root_node = KDTree()
# add items to tree...
networkx_graph(root_node)