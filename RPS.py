import random

def player(prev_play, opponent_history=[]):
    # Keep track of opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # If no history, play randomly
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # --- Advanced Strategy ---
    # 1. Detect if opponent cycles through moves (R->P->S or S->P->R)
    if len(opponent_history) > 5:
        last5 = opponent_history[-5:]
        if last5 == ["R", "P", "S", "R", "P"] or last5 == ["P", "S", "R", "P", "S"] or last5 == ["S", "R", "P", "S", "R"]:
            # Counter the next move in the cycle
            next_in_cycle = {"R": "P", "P": "S", "S": "R"}
            return next_in_cycle[opponent_history[-1]]

    # 2. Pattern recognition: look for repeated 2-move sequences
    if len(opponent_history) > 3:
        pattern = "".join(opponent_history[-2:])
        occurrences = [i for i in range(len(opponent_history)-2)
                       if opponent_history[i] == opponent_history[-2] and opponent_history[i+1] == opponent_history[-1]]
        if occurrences:
            next_moves = [opponent_history[i+2] for i in occurrences if i+2 < len(opponent_history)]
            if next_moves:
                prediction = max(set(next_moves), key=next_moves.count)
                return counter_move(prediction)

    # 3. If opponent repeats the same move, counter it
    if len(opponent_history) > 2 and opponent_history[-1] == opponent_history[-2]:
        return counter_move(opponent_history[-1])

    # 4. Fallback: counter the most common move
    most_common = max(set(opponent_history), key=opponent_history.count)
    return counter_move(most_common)

def counter_move(move):
    if move == "R":
        return "P"
    elif move == "P":
        return "S"
    else:
        return "R"
