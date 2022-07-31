# How to print a Sudoku 9*9

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 5, 0, 4, 0, 0, 0, 0, 1],
        [8, 7, 0, 9, 0, 6, 0, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 0, 0],
        [5, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 0, 3, 8],
        [4, 0, 0, 5, 6, 8, 9, 0, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 7],
        [6, 0, 3, 1, 9, 0, 2, 5, 0]]

def print_board(m):
    # If no board to print, print No Solution
    if m is None:
        print("No Solution")
        return
    line = '-'*25
    if m == []:
        print("Empty Matrix")
    num_of_rows = len(m)
    num_of_cols = len(m[0])

    for i in range (num_of_rows):
        # print line every 2 rows
        if i % 3 == 0:
            print(line)
        row_to_print = ""
        for j in range(num_of_cols):
            # print vertical bar every 2 column
            if j % 3 == 0:
                row_to_print += "| "
            value = str(m[i][j]) if m[i][j] > 0 else " "
            row_to_print += value + " "
        row_to_print += "|"
        print(row_to_print)
    print(line)

def possible(row, column, number):
    global board
    # Check the row for the same value
    for i in range(0, 9):
        if board[row][i] == number:
            return False

    # Check the column for the same value
    for i in range(0, 9):
        if board[i][column] == number:
            return False

    # Check the grid for the same value
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0 + i][x0 + j] == number:
                return False
    return True

def solve():
    global board
    for row in range(0, 9):
        for column in range(0, 9):
            if board[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0
                return
    print(print_board(board))
    input('More possible solutions')

solve()


