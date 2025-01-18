from linked_list import LinkedList

class Hashtable:
    def __init__(self):
        self.table = dict()

    def __str__(self):
        return f"{self.table}"

    def hash_function(self, value) -> str:
        result = 0
        for indx, item in enumerate(value):
            result += 17**indx * (sum([ord(item) for char in item]))
        result %= 28
        return str(result)

    def insert(self, value):
        value_hash = self.hash_function(value)
        print(value_hash)
        if not value in self.table.keys():
            self.table[value_hash] = LinkedList(value)
        else:
            new_node = LinkedList(value)
            new_node.next = self.table[value_hash]
            self.table[value_hash] = new_node
        
        return True
    
    def remove(self, value):
        value_hash = self.hash_function(value)
        self.table[value_hash]
        if value == self.table[value_hash].value:
            self.table[value_hash] = self.table[value_hash].next
        return True
    
    def search(self, value):
        value_hash = self.hash_function(value)
        return self.table[value_hash].search(value)


hash_table = Hashtable()

for item in ["link", "ilnk", "klin", "likn", "ilkn"]:
    hash_table.insert(item)

node = hash_table.search("link")
print(node, node.value)

hash_table.remove("klin")
print(hash_table)


