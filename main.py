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