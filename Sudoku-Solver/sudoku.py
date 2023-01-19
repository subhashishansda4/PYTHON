# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:38:12 2022

@author: VAGUE
"""

# printing the board for displaying the numbers
def print_board(puzzle):
    for r in range(len(puzzle)):
        if r%3 == 0 and r != 0:
            print("- - - - - - - - - - - -")
        
        for c in range(len(puzzle[0])):
            if c%3 == 0 and c != 0:
                print(" | ", end="")
                
            if c == 8:
                print(puzzle[r][c])
            else:
                print(str(puzzle[r][c]) + " ", end="")
                
def find_empty(puzzle):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None

# =============================================================================
# # checking sudoku rules
# def valid(puzzle, guess, pos):
#     # for checking every row
#     for i in range(len(puzzle[0])):
#         if puzzle[pos[0]][i] == guess and pos[1] != i:
#             return False
#      
#     # for checking every column
#     for i in range(len(puzzle)):
#         if(puzzle[i][pos[1]]) == guess and pos[0] != i:
#             return False
#          
#     # for checking every cube box
#     cube_x = pos[1] // 3
#     cube_y = pos[0] // 3
#     for i in range(cube_y*3, cube_y*3+3):
#         for j in range(cube_x*3, cube_x*3+3):
#             if puzzle[i][j] == guess and (i,j) != pos:
#                 return False
#      
#     return True
# =============================================================================

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = []
# =============================================================================
#     for i in range(len(puzzle)):
#         col_vals.append(puzzle[i][col])
# =============================================================================
    # using loop comprehension
    col_vals = [puzzle[i][col] for i in range(len(puzzle))]
    if guess in col_vals:
        return False
    
    row_start = (row//3)*3
    col_start = (col//3)*3
    
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    row, col = find_empty(puzzle)
    
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = 0
    
    return False

if __name__ == "__main__":
    board = [
        [0,0,6,8,0,2,0,0,4],
        [0,0,0,0,5,0,0,2,0],
        [0,8,0,0,1,0,0,0,0],
        [0,0,0,0,8,0,0,0,0],
        [0,0,4,0,0,0,3,0,0],
        [0,6,0,7,0,9,0,1,0],
        [9,0,0,0,0,0,0,0,1],
        [0,7,0,2,0,6,0,9,0],
        [0,0,0,0,0,5,0,0,0],
        ]
    
    print(solve_sudoku(board))
    print_board(board)