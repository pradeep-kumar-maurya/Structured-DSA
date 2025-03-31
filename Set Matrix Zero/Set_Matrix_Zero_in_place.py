def set_zero(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] == 0:
                if isinstance(matrix[0][j], str):
                    matrix[0][j] = '0'
                else:
                    matrix[0][j] = 0
                matrix[i][0] = str(matrix[i][0])

    for i in range(rows):
        for j in range(cols):

            if matrix[0][j] in ('0', 0):
                if isinstance(matrix[i][0], str):
                    matrix[i][j] = "0"
                else:
                    matrix[i][j] = 0

    for i in range(rows):
        for j in range(cols):

            if isinstance(matrix[i][0], str):
                matrix[i][j] = '0'

    for i in range(rows):
        for j in range(cols):

            if isinstance(matrix[i][j], str):
                matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zero(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zero(matrix)
print(matrix)

matrix = [[2, 4, 3],[1, 0, 0]]
set_zero(matrix)
print(matrix)

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
set_zero(matrix)
print(matrix)

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
set_zero(matrix)
print(matrix)

matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
set_zero(matrix)
print(matrix)
