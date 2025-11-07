from math import inf
from boop import Boop

def evaluate(state: Boop) -> int:
    if state.check_victory(silent=True):
        return inf if state.shift == 2 else -inf
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
    w_center = 2
    w_promo = 50
    score = (counts['cats_1'] * w_cat + counts['kittens_1'] * w_kitten) - (counts['cats_2'] * w_cat + counts['kittens_2'] * w_kitten)
    center_cells = [(1,1),(1,2),(2,1),(2,2)]
    for x, y in center_cells:
        if state.table[x][y] in (state.cat_1, state.kitten_1):
            score += w_center
        elif state.table[x][y] in (state.cat_2, state.kitten_2):
            score -= w_center
    promo_options = state.find_promotion_lines()
    if promo_options:
        if state.shift == 1:
            score += w_promo
        else:
            score -= w_promo
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