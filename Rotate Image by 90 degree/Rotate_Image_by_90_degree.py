def rotate(matrix):
    
    for i, row in enumerate(matrix):

        j = i + 1

        while j < len(row):

            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp

            j += 1

    for row in matrix:

        i = 0
        j = len(row) - 1

        while i <= j:
            temp = row[j]
            row[j] = row[i]
            row[i] = temp
            i += 1
            j -= 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

rotate(matrix)
print(matrix)
