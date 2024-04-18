
def tromino(n):
    matrix = [["X"] * 2**n for _ in range(2**n)]
    if n == 1:
        matrix[0][0]="G"
        matrix[1][0]="G"
        matrix[1][1]="G"
    elif n== 2:
        matrix[0][0]="Β"
        matrix[1][0]="Β"
        matrix[0][1]="Β"
        matrix[0][2]="R"
        matrix[0][3]="R"
        matrix[1][3]="R"
        matrix[2][0]="R"
        matrix[3][0]="R"
        matrix[3][1]="R"
        matrix[2][2]="Β"
        matrix[3][2]="Β"
        matrix[2][3]="Β"
        matrix[1][1]="G"
        matrix[2][1]="G"
        matrix[1][2]="G"
    elif n > 2:
        center_down_left = (2**n)//2
        matrix[center_down_left][center_down_left] = "G"
        matrix[center_down_left][center_down_left-1] = "G"
        matrix[center_down_left-1][center_down_left] = "G"
        

    for row in matrix:
        print(row)

tromino(4)