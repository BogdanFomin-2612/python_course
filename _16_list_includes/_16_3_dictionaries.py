# square_dict = {x: x ** 2 for x in range(10)}
# print(square_dict)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# transpose_matrix = {
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# }

transpose_matrix = []
# for i in range(len(matrix)):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transpose_matrix)

