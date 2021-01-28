"""
zhangyongguang
2020 11 13
"""
import _card_pool_manager
import _combo_score
from random import *
card_pool = {}

def cal_enemy_hit_rate(cards_on_table, enemy_number):
    global card_pool
    card_pool = _card_pool_manager._change_card_pool(cards_on_table, "on_table", card_pool)
    avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
    my_card = []
    rank = 10
    while rank != 2: # my power
        my_card = sample(avalible_cards, 2)
        my_combo = (cards_on_table).split(",") + my_card
        rank, combo_name = _combo_score.calculate_rank_power(my_combo)
    card_pool = _card_pool_manager._change_card_pool(",".join(my_card), "for_me", card_pool)
    card_pool_remember = card_pool.copy()
    hit = 0.0
    for _ in range(100000):
        card_pool = card_pool_remember.copy()
        for __ in range(enemy_number):
            avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
            p_card = sample(avalible_cards, 2)
            card_pool = _card_pool_manager._change_card_pool(",".join(p_card), "for_p1", card_pool)
            the_combo = (cards_on_table).split(",") + p_card
            rank, combo_name = _combo_score.calculate_rank_power(the_combo)
            if rank > 2: #enemy hit level
                hit += 1
                #print(the_combo, combo_name)
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
    enemy_number = 1
    card_pool = _card_pool_manager.refresh_card_pool()
    cards_on_table = "ht_2,cl_3,dm_5"
    start(cards_on_table, enemy_number)