class OpenAddressingHashtable:
    def __init__(self):
        self.keys_count = 28
        self.table = [None] * self.keys_count

    def __str__(self):
        return f"{self.table}"

    def hash_function(self, value) -> int:
        result = 0
        for indx, item in enumerate(value):
            result += 17**indx * ord(item)
        result %= self.keys_count 
        return result
    

    def insert(self, value):
        value_hash = self.hash_function(value)
        index = value_hash
        if not self.table[index]:
            self.table[index] = value
            return True

        next_value = self.table[index]
        while next_value:
            index += 1
            if index == self.keys_count:
                index = 0

            if index == value_hash:
                return False
            
            next_value = self.table[index]
        
        self.table[index] = value

   
    def search(self, value):
        value_hash = self.hash_function(value)
        index = value_hash

        if value == self.table[index]:
            return index
        
        next_value = self.table[index]
        while next_value:
            if next_value == value:
                return index
            index += 1
            if index == self.keys_count:
                index = 0

            if index == value_hash:
                return False
            
            next_value = self.table[index]
        
        return False

    
    def calculate_value_count(self):
        values_count = 0
        for value in self.table:
            if value:
                values_count += 1

        return values_count


    def load_factor(self):
        values_count = self.calculate_value_count()
        print(values_count)
        return values_count / self.keys_count
    
    def rehash(self):
        pass


hash_table = OpenAddressingHashtable()

for item in ["link", "ilnk", "klin", "likn", "ilkn"]:
    hash_table.insert(item)

print(hash_table)

index = hash_table.search("link")
print(index)

index = hash_table.search("osdf")
print(index)

print(hash_table.load_factor())
