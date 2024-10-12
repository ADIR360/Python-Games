import tkinter as tk
from tkinter import messagebox

# Check if a number can be placed in the position
def is_valid(board, row, col, num):
    # Check if the number is not in the current row, column, or 3x3 subgrid
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

# Create the GUI using Tkinter
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.current_row = 0
        self.current_col = 0
        self.create_grid()
        self.create_buttons()
        self.root.bind("<Key>", self.handle_keypress)

    # Create the grid where users can input numbers
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center", borderwidth=2)
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[row][col] = cell

    # Create buttons for solving and resetting the board
    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=10, column=0, columnspan=4)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        reset_button.grid(row=10, column=5, columnspan=4)

    # Retrieve the board from the user input
    def get_board(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[row][col].get()
                if value.isdigit():
                    self.board[row][col] = int(value)
                else:
                    self.board[row][col] = 0

    # Display the solved board back in the grid
    def display_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, str(self.board[row][col]))

    # Solve the Sudoku puzzle and update the grid
    def solve_puzzle(self):
        self.get_board()
        if solve_sudoku(self.board):
            self.display_board()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists.")

    # Reset the grid for a new puzzle
    def reset_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.board[row][col] = 0
        self.current_row = 0
        self.current_col = 0
        self.cells[self.current_row][self.current_col].focus_set()

    # Move through the grid using the arrow keys
    def handle_keypress(self, event):
        key = event.keysym
        if key == "Right":
            self.move_cursor(0, 1)
        elif key == "Left":
            self.move_cursor(0, -1)
        elif key == "Up":
            self.move_cursor(-1, 0)
        elif key == "Down":
            self.move_cursor(1, 0)
        elif key in "123456789":
            self.enter_number(key)

    # Move cursor based on keypress
    def move_cursor(self, row_delta, col_delta):
        new_row = self.current_row + row_delta
        new_col = self.current_col + col_delta

        if 0 <= new_row < 9 and 0 <= new_col < 9:
            self.current_row, self.current_col = new_row, new_col
            self.cells[self.current_row][self.current_col].focus_set()

    # Enter a number in the selected cell
    def enter_number(self, number):
        if self.board[self.current_row][self.current_col] == 0:
            self.cells[self.current_row][self.current_col].delete(0, tk.END)
            self.cells[self.current_row][self.current_col].insert(0, number)
            self.board[self.current_row][self.current_col] = int(number)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
