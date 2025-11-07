from math import inf
from boop import Boop

def evaluate(state: Boop) -> int:
    cats_1 = state.num_cats_1
    cats_2 = state.num_cats_2
    kittens_1 = state.num_kittens_1
    kittens_2 = state.num_kittens_2
    w_cat = 10
    w_kitten = 1
    score = (cats_1 * w_cat + kittens_1 * w_kitten) - (cats_2 * w_cat + kittens_2 * w_kitten)
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