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
    w_kitten = 2
    w_center = 1
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

def minimax(state: Boop, max_depth, depth=0, shift_max=True, alpha=-inf, beta=inf, best_move=None):
    if depth == max_depth or state.check_victory():
        score = evaluate(state)
        print(score)
        return score, best_move
    if shift_max == True and state.shift == 1:
        state.change_shift()
    if shift_max == False and state.shift == 2:
        state.change_shift()
    possible_moves = state.get_valid_moves()
    if shift_max:
        max_eval = -inf
        for move in possible_moves:
            print('max', move, state.shift)
            new_state, _ = state.simulate_move(move)
            eval, _ = minimax(new_state, max_depth, depth+1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        print('---', max_eval, best_move)
        return max_eval, best_move
    else:
        min_eval = inf
        for move in possible_moves:
            print('min', move, state.shift)
            new_state, _ = state.simulate_move(move)
            eval, _ = minimax(new_state, max_depth, depth+1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        print('---', min_eval, best_move)
        return min_eval, best_move

