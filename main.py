# Giải Sudoku bằng thuật toán quay lui (Backtracking)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):
    '''
    Giải 
    '''
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    # Lặp các giá trị 1->9 và điền vào các ô
    for i in range(1, 10):        
        if valid(bo, i, (row, col)):    # Kiểm tra các số điền vào có phải là số hợp lệ
            bo[row][col] = i

            if solve(bo):   # Hoàn thành giải pháp bằng Đệ quy 
                return True
            
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    '''
    Kiểm tra tính hợp lệ của con số khi đưa vào vị trí trong bảng
    bo: bảng
    num: số
    pos: vị trí
    '''
    # Kiểm tra trong hàng có bị trùng số khi thêm số vào
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Kiểm tra trong cột có bị trùng số khi thêm vào
    for i in range(len(bo)):
         if bo[i][pos[1]] == num and pos[0] != i:
                return False
    # Kiểm tra khối 3x3 các số không bị trùng nhau
    # Chuyển các hộp 3x3 thành mảng 2 chiều [0][0] -> [2][2]
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Lặp qua tất cả 9 phần tử trong hộp và đảm bảo các số không trùng nhau
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    '''
    In bảng Sudoku theo ma trận 2 chiều
    '''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:    # Check on the third row
            print("- - - - - - - - - - - - ")   # print a horizontal line
        for j in range(len(bo[0])):     # For every single position in the row
            if j % 3 == 0 and j != 0:   # Check if it the third kind of element or like a multiple of three
                print(" | ", end="")    # print a vertical line
            # print all numbers
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    '''
    Find some kind of empty square 
    '''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)   # row, col
    return None

print_board(board)
print("_________Solve_________")
solve(board)
print_board(board)


####################################################################
from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)
    
    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)