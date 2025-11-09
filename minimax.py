from boop import Boop

inf = float('inf')

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
    w_promo = 5
    score = (counts['cats_2'] * w_cat + counts['kittens_2'] * w_kitten) - (counts['cats_1'] * w_cat + counts['kittens_1'] * w_kitten)
    center_cells = [(1,1),(1,2),(2,1),(2,2)]
    for x, y in center_cells:
        if state.table[x][y] in (state.cat_1, state.kitten_1):
            score -= w_center
        elif state.table[x][y] in (state.cat_2, state.kitten_2):
            score += w_center
    promo_options = state.check_promotion()
    if promo_options:
        if state.shift == 1:
            score -= w_promo
        else:
            score += w_promo
    return score

def minimax(state: Boop, max_depth, depth=0, shift=True, alpha=-inf, beta=inf):
    if depth == max_depth:
        return
    possible_moves = state.get_valid_moves()
    if shift:
        max_eval = -inf
        best_move = None
        for move in possible_moves:
            print(move)
            new_state, answer = state.simulate_move(move)
            score = evaluate(new_state)
            print(score)
            if score > max_eval:
                max_eval = score
                best_move = move
    print(best_move)
    return best_move

