# q1

# Task 01: Tick-Tack-Toe Game
# Tic-Tac-Toe is a two-player game you already know about. Model the tic-tac-toe
# game between a user and a computer using Adversarial Search Algorithms.

import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[cond.index(cond[1])]] == player:
            if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
                return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Tic-Tac-Toe (User = X, AI = O)")
    print("Positions are numbered 0 to 8")
    print_board()

    while True:
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != " ":
            print("Invalid move! Try again.")
            continue

        board[user_move] = "X"
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move = best_move()
        board[ai_move] = "O"
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()