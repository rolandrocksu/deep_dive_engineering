import random
import sys

from binary_search_tree import Node

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

if __name__ == "__main__":
    test_instance = TestBinarySearchTree()
    tests_map = {
        "search": test_instance.test_search,
        "insert": test_instance.test_insertion,
        "isbst": test_instance.test_is_binary_search_tree,
        "remove_node": test_instance.test_remove_node,
        "miror": test_instance.test_miror
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