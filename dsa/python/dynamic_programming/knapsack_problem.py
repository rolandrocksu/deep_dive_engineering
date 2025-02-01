
class Knapsack:
    def __init__(self, size: int = 10, items_to_store: list = [(2, 1), (5, 2), (3, 3)]):
        self.size = size
        self.items = items_to_store
        B = [None] * (self.size+1)
        B[0] = 0

        self.obtaining_set = []

    def compute_maximal_bonuses(self):
        return self._compute_bonus_recursive(self.size)

    def _compute_bonus_recursive(self, Width: int):
        if Width == 0:
            return 0
        
        if Width < 0:
            return -100000
        
        optimal = max(
            [self._compute_bonus_recursive(Width - width) + bonus for width, bonus in self.items]
        )
        # obtaining_set.append(optimal)

        # B[W] = optimal

        return optimal

kp = Knapsack(10)
print(kp.compute_maximal_bonuses())
