"""
zhangyongguang
2020 11 2
"""
import _card_pool_manager
import _combo_score
import who_is_daddy
from random import *
card_pool = {}

def cal_enemy_hit_rate(cards_on_table, enemy_number):
    global card_pool
    card_pool = _card_pool_manager._change_card_pool(cards_on_table, "on_table", card_pool)
    avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
    my_card = []
    rank = 10
    while rank >= 3: # my power
        my_card = sample(avalible_cards, 2)
        combo_elements = cards_on_table.split(",") + my_card
        combos = who_is_daddy.generate_candidate_combo(combo_elements)
        my_combo, combo_name, rank, winner = who_is_daddy.find_max_combo(combos)
    card_pool = _card_pool_manager._change_card_pool(",".join(my_card), "for_me", card_pool)
    card_pool_remember = card_pool.copy()
    hit = 0.0
    for _ in range(100000):
        card_pool = card_pool_remember.copy()
        for __ in range(enemy_number):
            avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
            p_card = sample(avalible_cards, 2)
            combo_elements = cards_on_table.split(",") + p_card
            card_pool = _card_pool_manager._change_card_pool(",".join(p_card), "for_p1", card_pool)
            combos = who_is_daddy.generate_candidate_combo(combo_elements)
            his_combo, combo_name, rank, winner = who_is_daddy.find_max_combo(combos)
            if rank > 2: #enemy hit level
                hit += 1
                #print(combo_elements, combo_name)
                break
    print(hit / 100000, enemy_number)
    print(my_combo)
    return

def start():
    global card_pool
    card_pool = _card_pool_manager.refresh_card_pool()
    cards_on_table = input("input the cards on the table\t")
    enemy_number = input("input your enemy numbers\t")
    cal_enemy_hit_rate(cards_on_table, enemy_number)
    return

def start(cards_on_table, enemy_number):
    global card_pool
    card_pool = _card_pool_manager.refresh_card_pool()
    cal_enemy_hit_rate(cards_on_table, enemy_number)
    return

if __name__ == "__main__":
    for enemy_number in range(8):
        card_pool = _card_pool_manager.refresh_card_pool()
        cards_on_table = "dm_4,ht_5,ht_6,cl_4"
        enemy_number += 1
        start(cards_on_table, enemy_number)