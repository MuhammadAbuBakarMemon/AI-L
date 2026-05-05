# Task 02: Connect-Four
# Connect-four is a two-player game in which a user attempts to connect four balls
# horizontally, vertically, or diagonally in 6x7 game space. At each step a ball is
# placed at the lowest possible empty space a selected column. Model connect-four
# game between a user and a computer using Adversarial Search Algorithms.

import math

ROWS = 6
COLS = 7

board = [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
    print()
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("  " + "   ".join(str(i) for i in range(COLS)))
    print()

def is_valid_move(col):
    return board[0][col] == " "

def get_next_row(col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            return r

def drop_piece(row, col, piece):
    board[row][col] = piece

def check_winner(piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def is_draw():
    return all(board[0][c] != " " for c in range(COLS))

def evaluate_window(window, piece):
    score = 0
    opp = "X" if piece == "O" else "O"

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(" ") == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(" ") == 2:
        score += 2

    if window.count(opp) == 3 and window.count(" ") == 1:
        score -= 4

    return score

def score_position(piece):
    score = 0

    center = [board[r][COLS//2] for r in range(ROWS)]
    score += center.count(piece) * 3

    for r in range(ROWS):
        row = board[r]
        for c in range(COLS - 3):
            score += evaluate_window(row[c:c+4], piece)

    for c in range(COLS):
        col = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            score += evaluate_window(col[r:r+4], piece)

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def minimax(depth, alpha, beta, maximizing):
    if check_winner("O"):
        return 1000000
    if check_winner("X"):
        return -1000000
    if is_draw() or depth == 0:
        return score_position("O")

    if maximizing:
        value = -math.inf
        for col in range(COLS):
            if is_valid_move(col):
                row = get_next_row(col)
                drop_piece(row, col, "O")
                value = max(value, minimax(depth-1, alpha, beta, False))
                board[row][col] = " "
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return value
    else:
        value = math.inf
        for col in range(COLS):
            if is_valid_move(col):
                row = get_next_row(col)
                drop_piece(row, col, "X")
                value = min(value, minimax(depth-1, alpha, beta, True))
                board[row][col] = " "
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return value

def best_move():
    best_score = -math.inf
    move = 0
    for col in range(COLS):
        if is_valid_move(col):
            row = get_next_row(col)
            drop_piece(row, col, "O")
            score = minimax(4, -math.inf, math.inf, False)
            board[row][col] = " "
            if score > best_score:
                best_score = score
                move = col
    return move

def play_game():
    print("Connect Four (User = X, AI = O)")
    print_board()

    while True:
        col = int(input("Enter column (0-6): "))
        if not is_valid_move(col):
            print("Invalid move")
            continue

        row = get_next_row(col)
        drop_piece(row, col, "X")
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("Draw!")
            break

        ai_col = best_move()
        ai_row = get_next_row(ai_col)
        drop_piece(ai_row, ai_col, "O")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("Draw!")
            break

if __name__ == "__main__":
    play_game()