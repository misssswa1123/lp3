def is_safe(board, row, col, n):
   
    for i in range(row):
        if board[i][col] == 1:
            return False

   
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
  
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1         
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0          
    return False


n = int(input("Enter n: "))
first_col = int(input("Enter column for first queen (0 to n-1): "))


board = []
for i in range(n):
    board.append([0] * n)

board[0][first_col] = 1

if solve(board, 1, n):
    print("\nFinal N-Queens matrix:")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
else:
    print("No solution possible with the first queen at this position.")