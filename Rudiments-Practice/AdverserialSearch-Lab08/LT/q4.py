# Task 03: Mancala Game
# Mancala is a traditional two-player board game in which players collect and
# distribute small stone across a series of pts. Each player controls a row of pits
# and a storage area called ‘Mancala’. Players take turns picking up all the stones
# from one of their pits and placing them one by one into subsequent pits in a
# counterclockwise direction. The goal is to collect as many stones as possible in
# your mancala.
# The game involves strategic planning, as players can earn extra turns or capture
# their opponent’s stones based on where the last stone is placed. The game ends
# when the one side of the board is empty, and the player with the most stones in
# their mancala wins.
# Model Mancala game between a user and a computer using Adversarial Search
# Algorithms.

import math
import copy

PITS = 6

def initial_board():
    return [4]*PITS + [0] + [4]*PITS + [0]

def print_board(b):
    print()
    print("  ", end="")
    for i in range(12, 6, -1):
        print(f"{b[i]:2}", end=" ")
    print()
    print(f"{b[13]:2} {' ' * (PITS*3-1)} {b[6]:2}")
    print("  ", end="")
    for i in range(0, 6):
        print(f"{b[i]:2}", end=" ")
    print("\n")

def valid_moves(b, player):
    if player == 0:
        return [i for i in range(0, 6) if b[i] > 0]
    else:
        return [i for i in range(7, 13) if b[i] > 0]

def make_move(b, pit, player):
    b = copy.deepcopy(b)
    stones = b[pit]
    b[pit] = 0
    i = pit

    while stones > 0:
        i = (i + 1) % 14
        if player == 0 and i == 13:
            continue
        if player == 1 and i == 6:
            continue
        b[i] += 1
        stones -= 1

    if player == 0 and 0 <= i <= 5 and b[i] == 1:
        opp = 12 - i
        b[6] += b[opp] + 1
        b[i] = 0
        b[opp] = 0

    if player == 1 and 7 <= i <= 12 and b[i] == 1:
        opp = 12 - i
        b[13] += b[opp] + 1
        b[i] = 0
        b[opp] = 0

    extra_turn = (player == 0 and i == 6) or (player == 1 and i == 13)

    return b, extra_turn

def game_over(b):
    return sum(b[0:6]) == 0 or sum(b[7:13]) == 0

def evaluate(b):
    return b[6] - b[13]

def minimax(b, depth, maximizing, player):
    if depth == 0 or game_over(b):
        return evaluate(b)

    moves = valid_moves(b, player)

    if maximizing:
        value = -math.inf
        for m in moves:
            new_b, extra = make_move(b, m, player)
            val = minimax(new_b, depth-1, maximizing if extra else False, player if extra else 1-player)
            value = max(value, val)
        return value
    else:
        value = math.inf
        for m in moves:
            new_b, extra = make_move(b, m, player)
            val = minimax(new_b, depth-1, maximizing if extra else True, player if extra else 1-player)
            value = min(value, val)
        return value

def best_move(b):
    best_val = -math.inf
    move_choice = 0
    for m in valid_moves(b, 0):
        new_b, extra = make_move(b, m, 0)
        val = minimax(new_b, 4, True if extra else False, 0 if extra else 1)
        if val > best_val:
            best_val = val
            move_choice = m
    return move_choice

def play_game():
    b = initial_board()
    player = 0

    print("Mancala (User = Bottom row, AI = Top row)")
    print_board(b)

    while not game_over(b):
        if player == 0:
            move = int(input("Choose pit (0-5): "))
            if move not in valid_moves(b, 0):
                print("Invalid move")
                continue
            b, extra = make_move(b, move, 0)
            print_board(b)
            if not extra:
                player = 1
        else:
            move = best_move(b)
            print("AI chooses pit:", move)
            b, extra = make_move(b, move, 1)
            print_board(b)
            if not extra:
                player = 0

    b[6] += sum(b[0:6])
    b[13] += sum(b[7:13])
    for i in range(0,6):
        b[i] = 0
    for i in range(7,13):
        b[i] = 0

    print_board(b)

    if b[6] > b[13]:
        print("You win!")
    elif b[6] < b[13]:
        print("AI wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    play_game()