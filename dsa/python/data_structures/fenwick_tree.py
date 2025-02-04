from pprint import pprint

class FenwickTree:
    
    def __init__(self):
        self.values = [i for i in range(30)]
        self.all_levels = [self.values]

    def construct_tree(self, aggregate_func):
        current_level = self.values
        while True:
            next_level = []
            for i in range(1, len(current_level)):
                if len(current_level) % 2 and i == len(current_level)-1:
                    next_level.insert(i, current_level[i])
                elif i % 2:
                    current_value = current_level[i]
                    next_value = current_level[i-1]
                    next_level.insert(i, aggregate_func(next_value, current_value))
                
            current_level = next_level
            self.all_levels.append(current_level)
            if len(current_level) == 1:
                break

        for item in self.all_levels:
            print(item)

    def get_max(self, from_index: int, to_index: int):
        values = []
        to_index -= 1
        for level in self.all_levels:
            print(from_index, "<<<<<<<")

            if from_index % 2:
                values.append(level[from_index])
                from_index += 1
            
            if not to_index % 2:
                values.append(level[to_index])
                to_index -= 1

            from_index //= 2
            to_index //= 2

            if to_index < from_index:
                break

        print(">>>", values)
        

tree = FenwickTree()
tree.construct_tree(max)
tree.get_max(3, 11)







