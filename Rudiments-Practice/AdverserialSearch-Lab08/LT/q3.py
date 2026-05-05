# Task 03: Nim Game
# Nim is a two-player mathematical game in which a pile of objects is given to
# players. Each player is allowed to remove 1,2 or 3 objects at each turn. On who
# remove the last object will win the game. Model nim game between a user and a
# computer using Adversarial Search Algorithms.

import math

def minimax(n, is_maximizing):
    if n == 0:
        return -1 if is_maximizing else 1

    if is_maximizing:
        best = -math.inf
        for move in [1, 2, 3]:
            if n - move >= 0:
                best = max(best, minimax(n - move, False))
        return best
    else:
        best = math.inf
        for move in [1, 2, 3]:
            if n - move >= 0:
                best = min(best, minimax(n - move, True))
        return best

def best_move(n):
    best_val = -math.inf
    move_choice = 1
    for move in [1, 2, 3]:
        if n - move >= 0:
            value = minimax(n - move, False)
            if value > best_val:
                best_val = value
                move_choice = move
    return move_choice

def play_game():
    n = int(input("Enter initial number of objects: "))
    turn = "user"

    while n > 0:
        print("Remaining:", n)

        if turn == "user":
            move = int(input("Take 1, 2, or 3: "))
            if move not in [1,2,3] or move > n:
                print("Invalid move")
                continue
            n -= move
            if n == 0:
                print("You win!")
                break
            turn = "ai"

        else:
            move = best_move(n)
            print("AI takes:", move)
            n -= move
            if n == 0:
                print("AI wins!")
                break
            turn = "user"

if __name__ == "__main__":
    play_game()