# Valid Chess board

def check_board(matrix):
    base = matrix[0][0]

    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if ((i+j)%2==0):
                if matrix[i][j]!=base:
                    return False
            else: 
                if matrix[i][j] == base:
                    return False
    return True


board1 = [[0, 1], [1, 0]]
board2 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
board3 = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]

print("true" if check_board(board1) else "false")
print("true" if check_board(board2) else "false")
print("true" if check_board(board3) else "false")
                            
