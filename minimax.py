from math import inf
from boop import Boop

def evaluate(state: Boop) -> int:
    if state.check_victory():
        if state.shift == 2:
            return inf
        else:
            return -inf
    counts = {
        "cats_1": 0,
        "cats_2": 0,
        "kittens_1": 0,
        "kittens_2": 0
    }
    for row in state.table:
        counts['cats_1'] += row.count(state.cat_1)
        counts['cats_2'] += row.count(state.cat_2)
        counts['kittens_1'] += row.count(state.kitten_1)
        counts['kittens_2'] += row.count(state.kitten_2)
    w_cat = 10
    w_kitten = 1
    score = (counts['cats_1'] * w_cat + counts['kittens_1'] * w_kitten) - (counts['cats_2'] * w_cat + counts['kittens_2'] * w_kitten)
    return score

def minimax(state: Boop, depth: int, alpha: float, beta: float, maximizing: bool):
    if depth == 0 or state.check_victory():
        return evaluate(state), None
    moves = state.get_valid_moves()
    if not moves:
        return evaluate(state), None
    if maximizing:
        max_eval = -inf
        best_move = None
        for move in moves:
            new_state, info = state.simulate_move(move)
            eval_score, _ = minimax(new_state, depth-1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = inf
        best_move = None
        for move in moves:
            new_state, info = state.simulate_move(move)
            eval_score, _ = minimax(new_state, depth-1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move