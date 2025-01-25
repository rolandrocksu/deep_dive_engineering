class OpenAddressingHashtable:
    def __init__(self, size=28):
        self.keys_count = size
        self.values_count = 0
        self.table = [None] * self.keys_count

    def __str__(self):
        return f"{self.table}"
    
    def visualize_table(self):
        print(''.join(["*" if i else " " for i in self.table ]))

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
        else:
            next_value = self.table[index]
            while next_value:
                index += 1
                if index == self.keys_count:
                    index = 0

                if index == value_hash:
                    return False
                
                next_value = self.table[index]
        
            self.table[index] = value
    
        self.values_count += 1
        if not self.values_count % 10:
            if self.load_factor() > 0.75:
                self.rehash()
        return True


   
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
        # values_count = self.calculate_value_count()
        return self.values_count / self.keys_count
    
    def runs_length(self):
        runs_length = []
        current = 0
        for ind, cell in enumerate(self.table):
            if cell is None:
                index, start = ind, ind
                break

        while True:
            index += 1
            if index == self.keys_count:
                index = 0

            if index == start:
                break
            print(index, self.table[index] )
            if self.table[index] is not None:
                current +=1
            else:
                if current:
                    runs_length.append(current)
                current = 0

        return runs_length
            



    def rehash(self):
        old_table = self.table
        self.keys_count *= 2
        self.values_count = 0
        self.table = [None] * self.keys_count

        for item in old_table:
            if item:
                self.insert(item)
        
    
    def lazy_rehash(self):
        pass

    def remove(self, value):
        value_hash = self.hash_function(value)
        index = value_hash

        if self.table[index] == value:
            # Remove the value and place a marker to preserve probe sequence
            self.table[index] = None
            self.values_count -= 1
            return True

        while True:
            index += 1
            next_value = self.table[index]
            pass
