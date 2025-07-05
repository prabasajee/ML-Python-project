# Example main.py for testing RPS player
from RPS import player
import random

def random_bot(prev_play, _=[]):
    return random.choice(["R", "P", "S"])

def play(player1, player2, num_games=100, verbose=False):
    p1_history = []
    p2_history = []
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0
    for i in range(num_games):
        move1 = player1(p2_prev, p2_history)
        move2 = player2(p1_prev, p1_history)
        p1_history.append(move1)
        p2_history.append(move2)
        p1_prev = move1
        p2_prev = move2
        if verbose:
            print(f"Game {i+1}: Player1={move1}, Player2={move2}")
        if move1 == move2:
            continue
        elif (move1 == "R" and move2 == "S") or (move1 == "P" and move2 == "R") or (move1 == "S" and move2 == "P"):
            p1_score += 1
        else:
            p2_score += 1
    print(f"Final Score: Player1={p1_score}, Player2={p2_score}")

if __name__ == "__main__":
    play(player, random_bot, 100, verbose=True)
