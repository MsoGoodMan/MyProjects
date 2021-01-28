"""
zhangyongguang
2020 11 13
"""
from itertools import combinations
import _combo_score

def generate_candidate_combo(combo_elements):
    combos = list(combinations(combo_elements, 5))
    return combos

def find_max_combo(combos):
    if len(combos) == 0:
        print("FATAL ERROR -> who_is_daddy.find_max_combo: candidate_combo_list length is 0")
    max_combo = []
    high_rank_combos = []
    max_rank = 0
    max_combo_name = "high_card"
    player_index = 0
    rank_winner = []
    final_winner = []
    for combo in combos:
        rank, combo_name = _combo_score.calculate_rank_power(combo)
        if rank == max_rank:
            high_rank_combos.append(combo)
            rank_winner.append(player_index)
            max_rank = rank
            max_combo_name = combo_name
        if rank > max_rank:
            high_rank_combos = []
            high_rank_combos.append(combo)
            rank_winner = []
            rank_winner.append(player_index)
            max_rank = rank
            max_combo_name = combo_name
        player_index += 1
    if len(high_rank_combos) > 1:
        max_kick_power = -1
        rank_winner_index = 0
        for combo in high_rank_combos:
            kick_power = _combo_score.calculate_kicks_power(combo, max_rank)
            if kick_power == max_kick_power:
                max_combo.append(combo)
                final_winner.append(rank_winner[rank_winner_index])
            if kick_power > max_kick_power:
                max_combo = []
                max_combo.append(combo)
                max_kick_power = kick_power
                final_winner = []
                final_winner.append(rank_winner[rank_winner_index])
            rank_winner_index += 1
    else:
        max_combo = high_rank_combos
        final_winner = rank_winner
    return max_combo, max_combo_name, max_rank, final_winner

def dual(element_lists):
    combos = []
    for combo_elements in element_lists:
        combo_candidates = generate_candidate_combo(combo_elements)
        his_max_combo, his_max_combo_name, his_max_rank, his_final_winner = find_max_combo(combo_candidates)
        combos.append(his_max_combo[0])
    his_max_combo, his_max_combo_name, his_max_rank, his_final_winner = find_max_combo(combos)
    return his_max_combo, his_max_combo_name, his_max_rank, his_final_winner

if __name__ == "__main__":
    # combo_elements = ['sp_8', 'dm_6', 'cl_6', 'cl_7', 'cl_4', 'dm_8', 'ht_8']
    # combos = generate_candidate_combo(combo_elements)
    # high_rank_combos, max_combo_name, max_rank, final_winner = find_max_combo(combos)
    # print(high_rank_combos, max_combo_name, max_rank)
    p1 = ['cl_14', 'sp_13', 'cl_12', 'cl_3', 'cl_7', 'cl_9', 'dm_12']
    p2 = ['ht_14', 'sp_14', 'cl_12', 'cl_3', 'cl_7', 'cl_9', 'dm_12']
    combos = [p1, p2]
    high_rank_combos, max_combo_name, max_rank, final_winner = dual(combos)
    print(high_rank_combos)
