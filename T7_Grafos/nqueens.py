from typing import List, Iterator
import time

######### VARIABLE CONVENTIONS #########

## n: side of the board (n x n)
## i: iterate over rows
## j: iterate over columns
## row: candidate row being explored
## col: candidate column being explored
## board: List[List[int]] such that:
##     board[row][col] = 1 if there is a queen at position (row, col)
##     board[row][col] = 0 otherwise

########################################


def is_valid(n: int, board: List[List[int]], row: int, col: int) -> bool:
    is_good: bool = True
    i: int = 0
    j: int = 0
    # Check if there is a queen in the same row
    while j < col and is_good:
        if board[row][j] == 1:
            is_good = False
        j += 1
    # Check if there is a queen in the diagonal above
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0 and is_good:
        if board[i][j] == 1:
            is_good = False
        i -= 1
        j -= 1
    # Check if there is a queen in the diagonal below
    i = row + 1
    j = col - 1
    while i < n and j >= 0 and is_good:
        if board[i][j] == 1:
            is_good = False
        i += 1
        j -= 1

    return is_good


def solve_queens_problem(n: int) -> None:
    board: List[List[int]] = [[0 for i in range(n)] for j in range(n)]
    start = time.time()
    found: bool = solve_queens_aux(n, board, 0)
    end = time.time()
    elapsed_time: float = (end - start) * 1e3
    if found:
        print("Solution found for n = " + str(n))
        print("In " + str(elapsed_time) + " ms.")
        for i in range(n):
            print(board[i])
    else:
        print("Solution NOT found for n = " + str(n))
        print("In " + str(elapsed_time) + " ms.")


def solve_queens_aux(n: int, board: List[List[int]], col: int) -> bool:
    if col == n:
        return True
    found: bool = False
    row: int = 0
    while row < n and not found:
        if is_valid(n, board, row, col):
            board[row][col] = 1
            if solve_queens_aux(n, board, col + 1):
                found = True
            else:
                # Revert the attempt
                board[row][col] = 0
        row += 1
    return found


solve_queens_problem(4)