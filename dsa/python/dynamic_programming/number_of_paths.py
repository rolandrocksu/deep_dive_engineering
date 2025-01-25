

def get_number_of_paths(i=0, j=0):
    rows = 10
    cols = 10
    matrix = [[0 for _ in range(10)] for _ in range(10)]

    if j == len(rows)-1:
        return 1
    
    if i == len(matrix)-1:
        return 1
    
    if matrix[i+1][j]:
        return get_number_of_paths(i, j+1)
    elif matrix[i][j+1]:
        return get_number_of_paths(i, j+1)
    else:
        return get_number_of_paths(i+1, j) + get_number_of_paths(i, j+1)


# print(get_number_of_paths())




from random import randint
from pprint import pprint
matrix = [
    [" " for _ in range(10)] for _ in range(10)
]

for _ in range(40):
    matrix[randint(0, 9)][randint(0, 9)] = "*"

pprint(matrix)

def get_number_of_paths_dp():
    rows = len(matrix) - 1 
    cols = len(matrix[0]) - 1

    values_matrix = [
        [-1 for _ in range(10)] for _ in range(10)
    ]
    values_matrix[rows][cols] = 1

    for i in range(cols-1, -1, -1):
        if matrix[rows][i] != "*":
            values_matrix[rows][i] = values_matrix[rows][i+1]
        else:
            values_matrix[rows][i] = 0
    
    for j in range(rows-1, -1, -1):
        if matrix[j][cols] != "*":
            values_matrix[j][cols] = values_matrix[j + 1][cols]
        else:
            values_matrix[j][cols] = 0

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if matrix[i][j] != "*":
                values_matrix[i][j] = values_matrix[i+1][j] + values_matrix[i][j+1]
            else:
                values_matrix[i][j] = 0

    return values_matrix
            

pprint(get_number_of_paths_dp())

