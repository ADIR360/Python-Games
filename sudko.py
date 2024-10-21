# Check if a number can be placed in the position
def is_valid(board, row, col, num):
    # Check if the number is not in the current row, column, and 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    
    return True

# Brute force Sudoku solver using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty space
                for num in range(1, 10):  # Try all numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        
                        board[row][col] = 0  # Backtrack
                return False
    return True

# User input for pre-filled number and its position
def input_number(board):
    row = int(input("Enter row (0-8): "))
    col = int(input("Enter column (0-8): "))
    num = int(input("Enter number (1-9): "))
    
    if is_valid(board, row, col, num):
        board[row][col] = num
    else:
        print("Invalid input, try again.")
        input_number(board)

# Example empty Sudoku board (0 means empty)
sudoku_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Input predefined numbers
input_number(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
