
class LinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def add(self, value):
        new_node = LinkedList(value)
        self.next = new_node
        return new_node

    def search(self, value):
        node = self
        while node:
            if value == node.value:
                return node
            node = node.next
        
        return None
    
    def remove(self, value):
        node = self
        preveous = self
        while node:
            if value == node.value:
                preveous.next = node.next
                break
            preveous = node
            node = node.next

        
        return None