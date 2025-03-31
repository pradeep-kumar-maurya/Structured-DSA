def set_zero(matrix):
    
    rows_with_zero = set()
    cols_with_zero = set()
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):

        for j in range(cols):

            if matrix[i][j] == 0:
                rows_with_zero.add(i)
                cols_with_zero.add(j)

    for i in range(rows):

        for j in range(cols):

            if i in rows_with_zero:
                matrix[i][j] = 0
            if j in cols_with_zero:
                matrix[i][j] = 0
        

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zero(matrix))
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zero(matrix))
print(matrix)

matrix = [[2, 4, 3],[1, 0, 0]]
print(set_zero(matrix))
print(matrix)

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(set_zero(matrix))
print(matrix)
