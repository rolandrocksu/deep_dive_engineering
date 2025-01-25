
W = 10
W_items = [(2, 1), (5, 2), (3, 3)]
B = [None] * (W+1)
B[0] = 0

obtaining_set = []

def knapsack(W: int):

    if W == 0:
        return 0
    
    if W < 0:
        return -100000
    
    optimal = max(
        [knapsack(W - w) + b for w, b in W_items]
    )
    # obtaining_set.append(optimal)

    # B[W] = optimal

    return optimal


print(knapsack(W))


# print(obtaining_set)
# print(B)
