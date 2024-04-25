
def tromino(n):
    matrix = [["X"] * 2**n for _ in range(2**n)]
    if n == 1:
        matrix[0][0]="G"
        matrix[1][0]="G"
        matrix[1][1]="G"
    elif n== 2:
        matrix = [["B", "B", "R", "R"],
                  ["B", "G", "G", "R"],
                  ["R", "G", "B", "B"],
                  ["R", "R", "B", "X"]]

    elif n == 3:
        matrix = [["B", "B", "R", "R"],
                  ["B", "G", "G", "R"],
                  ["R", "G", "B", "B"],
                  ["R", "R", "B", "X"]]
        def rotate_90(matrix):
             transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
             rotated_matrix = [row[::-1] for row in transposed]
             return rotated_matrix
        matrix2 = rotate_90(matrix)
        def replace_colors(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == "R":
                        matrix[i][j] = "B"
                    elif matrix[i][j] == "B":
                        matrix[i][j] = "R"
        
        replace_colors(matrix2)
        def rotate_180(matrix):
            rotated_matrix180 = matrix
            for i in range(2):
                rotated_matrix180 = rotate_90(rotated_matrix180)
            return rotated_matrix180
        matrix3 = rotate_180(matrix)
        def rotate_270(matrix):
            rotated_matrix270 = matrix
            for i in range(3):
                rotated_matrix270 = rotate_90(rotated_matrix270)
            return rotated_matrix270
        matrix4 = rotate_270(matrix)
        replace_colors(matrix4)

        merged_matrix = []
        # Ενώνουμε τον δεύτερο πίνακα στον πρώτο
        for i in range(len(matrix)):
            merged_matrix.append(matrix[i] + matrix2[i])
        for row in range(len(matrix4)):
            merged_matrix.append(matrix4[row] ) 
        for i in range(len(matrix3)):
            merged_matrix[len(matrix) + i] += matrix3[i]
        matrix = merged_matrix
        
  
    
    for row in matrix:
        print(row)
        
tromino(3)

