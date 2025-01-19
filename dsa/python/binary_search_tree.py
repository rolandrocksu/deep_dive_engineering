
import random


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def __str__(self):
        return f"Node(value={self.value}, parent={self.parent.value if self.parent else self.parent})"


    def insert_value_iterative(self, value):
        node_to_add = self
        while True:
            if node_to_add.value < value:
                if not node_to_add.right:
                    node_to_add.right = Node(value, parent=node_to_add)
                    node_to_add = node_to_add.right
                    break
                node_to_add = node_to_add.right
                continue
            elif node_to_add.value >= value:
                if not node_to_add.left:
                    node_to_add.left = Node(value, parent=node_to_add)
                    node_to_add = node_to_add.left
                    break 
                node_to_add = node_to_add.left
                continue

        return node_to_add

    def insert_value_recursively(self, value):
        if self.value >= value:
            if not self.left:
                self.left = Node(value, parent=self)
            else:
                self.left.insert_value_recursively(value)
        else:
            if not self.right:
                self.right = Node(value, parent=self)
            else:
                self.right.insert_value_recursively(value)


    def search_value_iterative(self, value):
        while True:
            if self.value == value:
                return self
            if self.value < value:
                if not self.right:
                    return False
                self = self.right
                continue
            elif self.value > value:
                if not self.left:
                    return False
                self = self.left
                continue

    def search_value_recursively(self, value):
        if self.value == value:
            return self
        if self.value < value:
            if not self.right:
                return False
            return self.right.search_value_recursively(value)
        elif self.value > value:
            if not self.left:
                return False
            return self.left.search_value_recursively(value)
    
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
    
    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current
    
    def is_bst(self):
        if self.right:
            if self.right.value < self.value:
                return False
            self.right.is_bst()
        if self.left:
            if self.left.value > self.value:
                return False
            self.left.is_bst()
        
        return True
    
    @staticmethod
    def remove_node(node):
        if node.left and node.right:
            min_node = node.right.find_min()
            node.right.parent = min_node
            if node.value > node.parent.value:
                node.parent.right = min_node
            else:
                if node.left.left:
                    node.left.parent = min_node
                node.parent.left = min_node
            
        elif node.left:
            if node.value > node.parent.value:
                node.parent.right = node.left
            else:
                node.parent.left =  node.left
        elif node.right:
            if node.value > node.parent.value:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
        else:
            if node.value > node.parent.value:
                node.parent.right = None
            else:
                node.parent.left = None

    def miror_recursively(self):
        self.left, self.right = self.right, self.left
        self.left and self.left.miror_recursively()
        self.right and self.right.miror_recursively()

    def miror_iterative(self):
        current_layer = [self]
        while current_layer:
            next_layer = []

            for node in current_layer:
                node.left, node.right = node.right, node.left

                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
    
            current_layer = next_layer
    
    def inorder_traversal(self):
        result = []
        if self.left:
            result += self.left.inorder_traversal()

        result.append(self.value)
        
        if self.right:
            result += self.right.inorder_traversal()
        
        return result
    
    def preorder_traversal(self):
        result = []

        result.append(self.value)

        if self.left:
            result += self.left.preorder_traversal()

        if self.right:
            result += self.right.preorder_traversal()

        return result


    def next_inorder(self):

        if self.right:
            return self.right.find_min()

        current = self

        while current and current == current.parent.right:
            current = current.parent

        return current.parent
    
    def next_preorder(self):
        if self.left:
            return self.left
        
        if self.right:
            return self.right
        
        current = self
        while current.parent:
            if current == current.parent.left and current.parent.right:
                return current.parent.right
            current = current.parent

        return None

    

    def max_depth(self):
        if self.left is None and self.right is None:
            return 0
        if self.left and self.right:
            return 1 + max(self.left.max_depth(), self.right.max_depth())
        
        if self.left:
            return 1 + self.left.max_depth()
        if self.right:
            return 1 + self.right.max_depth()
    
    def min_depth(self):
        if self.left is None and self.right is None:
            return 0
        if self.left and self.right:
            return 1 + min(self.left.min_depth(), self.right.min_depth())
        
        if self.left:
            return 1 + self.left.min_depth()
        if self.right:
            return 1 + self.right.min_depth()
        

    def calculate_balanceness(self):
        max_depth = self.max_depth()
        min_depth = self.min_depth()
        
        if max_depth == 0:
            return 0
        return min_depth / max_depth
