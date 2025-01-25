from dsa.python.simple_data_structures.linked_list import LinkedList

class Hashtable:
    def __init__(self):
        self.table = dict()
        self.keys_count = 28
        self.values_count = 0
        self.status = "normal"

    def __str__(self):
        return f"{self.table}"

    def hash_function(self, value) -> str:
        result = 0
        for indx, item in enumerate(value):
            result += 17**indx * ord(item)
        result %= self.keys_count 
        return str(result)

    def insert(self, value):
        value_hash = self.hash_function(value)
        if not value_hash in self.table.keys():
            self.table[value_hash] = LinkedList(value)
        else:
            new_node = LinkedList(value)
            new_node.next = self.table[value_hash]
            self.table[value_hash] = new_node

        self.values_count += 1
        if not self.values_count % 10:
            if self.load_factor() > 1.5:
                self.rehash()
        return True
    
    def remove(self, value):
        value_hash = self.hash_function(value)
        self.table[value_hash]
        if value == self.table[value_hash].value:
            self.table[value_hash] = self.table[value_hash].next

        # TODO
        
        self.values_count -= 1
        return True
    
    def search(self, value):
        value_hash = self.hash_function(value)
        return self.table[value_hash].search(value)
    
    def calculate_value_count(self):
        values_count = 0
        for value in self.table.values():
            current = value
            while current:
                values_count +=1
                current = current.next

        return values_count

    def load_factor(self):
        # values_count = self.calculate_value_count()
        return self.values_count / self.keys_count
    
    def rehash(self):
        old_table = self.table
        self.keys_count *= 2
        self.table = dict()
        self.values_count = 0

        for value in old_table.values():
            current = value
            while current:
                self.insert(current.value)
                current = current.next
    
    def lazy_rehash(self):
        pass


hash_table = Hashtable()

for item in ["link", "ilnk", "klin", "likn", "ilkn"]:
    hash_table.insert(item)

node = hash_table.search("link")
print(node, node.value)

hash_table.remove("klin")
print(hash_table)

print(hash_table.load_factor())

