import random
import sys

from dsa.python.simple_data_structures.binary_search_tree import Node

class TestBinarySearchTree:

    def __init__(self, root_value=200):
        self.root = Node(root_value)
        self.nodes_list = []
        for value in [100, 400, 500, 300, 450, 350, 120, 90, 70, 95]:
            self.nodes_list.append(self.root.insert_value_iterative(value))

    
    def test_search(self, value=70):
        print(f"\n[Test] Searching for node with value {value}")
        searched_node_iterative = self.root.search_value_iterative(value)

        print(f"Iterative Search Result: {searched_node_iterative}")

        searched_node_recursive = self.root.search_value_recursively(value)

        print(f"Recursive Search Result: {searched_node_recursive}")


    def test_is_binary_search_tree(self):

        result = self.root.is_bst()
        print(f"This should be true --> {result}")

        
    def test_insertion(self):
        inserted_node = self.root.insert_value_iterative(12)
        print(inserted_node)

        self.root.insert_value_recursivly(12)
        print(self.root.search_value_recursivly(12))

        for i in (random.randint(1, 100) for _ in range(100)):
            inserted_node = self.root.insert_value_iterative(i)
            # print(inserted_node)

        for i in (random.randint(1, 100) for _ in range(100)):
            inserted_node = self.root.insert_value_recursivly(i)

        print(self.root)


    def test_remove_node(self):
        print("BEFORE Remove")
        for nd in self.nodes_list:
            print(nd)

        self.root.remove_node(self.nodes_list[0])

        print("AFTER Remove")

        for nd in self.nodes_list:
            print(nd)

    def test_miror(self):
        print("-- Miroring iterative --")
        self.root.miror_iterative()
        print("-- Miroring recursively --")
        self.root.miror_recursively()

    def test_traversal(self):
        print("-- Traversal --")
        res = self.root.inorder_traversal()
        print(f"Inorder Traversal: {self.root.inorder_traversal()}")
        print(f"Preorder Traversal: {self.root.preorder_traversal()}")
    
    def test_next_inorder(self):
        print("-- Next in Order --")
        res = self.root.next_inorder()

        in_order_nodes = self.root.inorder_traversal()
        print(f"Inorder Traversal: {in_order_nodes}")

        for i, value in enumerate(in_order_nodes):
            node = self.root.search_value_iterative(value)
            successor = node.next_inorder()
            successor_value = successor.value if successor else None
            expected_successor = in_order_nodes[i + 1] if i + 1 < len(in_order_nodes) else None
            print(f"Node: {node.value}, Expected Successor: {expected_successor}, Actual Successor: {successor_value}")

    def test_next_preorder(self):
        print("-- Testing Next Preorder --")
        
        preorder_nodes = self.root.preorder_traversal()
        print(f"Preorder Traversal: {preorder_nodes}")
        
        node = self.root
        actual_preorder = []
        while node:
            actual_preorder.append(node.value)
            node = node.next_preorder()
        
        print(f"Actual Preorder Using next_preorder: {actual_preorder}")

    def test_calculate_balanceness(self):
        res = self.root.calculate_balanceness()

if __name__ == "__main__":
    test_instance = TestBinarySearchTree()
    tests_map = {
        "search": test_instance.test_search,
        "insert": test_instance.test_insertion,
        "isbst": test_instance.test_is_binary_search_tree,
        "remove_node": test_instance.test_remove_node,
        "miror": test_instance.test_miror,
        "traversal": test_instance.test_traversal,
        "next_inorder": test_instance.test_next_inorder,
        "next_preorder": test_instance.test_next_preorder,
        "calculate_balanceness": test_instance.test_calculate_balanceness,
    }

    if len(sys.argv) < 2:
        print("Usage: python test_binary_search_tree.py <test_name>")
        print("Available tests: search, insert, isbst, remove_node")
        sys.exit(1)

    test_name = sys.argv[1]
    if test_name in tests_map:
        print(f"Running test: {test_name}")
        tests_map[test_name]()
    else:
        print(f"Invalid test name: {test_name}")
        print("Available tests: search, insert, isbst, remove_node")
        sys.exit(1)