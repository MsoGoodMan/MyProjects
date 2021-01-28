"""
zhangyongguang
2020 12 17
"""
import _card_pool_manager
import who_is_daddy
from random import *
import _tools
card_pool = {}

def start(cards_on_table, p1_cards, p2_cards):
    global card_pool
    card_pool = _card_pool_manager.refresh_card_pool()
    table_cards = len(cards_on_table.split(","))
    if cards_on_table != "":
        card_pool = _card_pool_manager._change_card_pool(cards_on_table, "on_table", card_pool)
    else:
        table_cards = 0
    card_pool = _card_pool_manager._change_card_pool(p1_cards, "for_p1", card_pool)
    card_pool = _card_pool_manager._change_card_pool(p2_cards, "for_p2", card_pool)
    avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
    pad_num = 5 - table_cards
    p1_win = 0.0
    p2_win = 0.0
    draw_game_times = 0.0
    for _ in range(100000):
        p1_win_times = 0.0
        p2_win_times = 0.0
        sub_card_pool = card_pool.copy()
        comming_card = sample(avalible_cards, pad_num)
        sub_card_pool = (_card_pool_manager._change_card_pool(",".join(comming_card), "on_the_table", sub_card_pool))
        sub_avalible_cards = _card_pool_manager._get_valid_cards(sub_card_pool)
        p1_element_list = _tools.trim_cards_for_user(cards_on_table, p1_cards, comming_card)
        p2_element_list = _tools.trim_cards_for_user(cards_on_table, p2_cards, comming_card)
        player_element_list_r1 = p1_element_list + p2_element_list
        max_combo, combo_name, rank, winner = who_is_daddy.dual(player_element_list_r1)
        if 0 in winner:
            p1_win_times += 1.0
        if 1 in winner:
            p2_win_times += 1.0
        comming_card = sample(sub_avalible_cards, pad_num)
        p1_element_list = _tools.trim_cards_for_user(cards_on_table, p1_cards, comming_card)
        p2_element_list = _tools.trim_cards_for_user(cards_on_table, p2_cards, comming_card)
        player_element_list_r2 = p1_element_list + p2_element_list
        max_combo, combo_name, rank, winner = who_is_daddy.dual(player_element_list_r2)
        if 0 in winner:
            p1_win_times += 1.0
        if 1 in winner:
            p2_win_times += 1.0
        if p1_win_times > p2_win_times:
            p1_win += 1
        elif p2_win_times > p1_win_times:
            p2_win += 1
        else:
            draw_game_times += 1
    print("p1 --> twice all in --> no return --> win rate " + str(p1_win / 100000))
    print("p2 --> twice all in --> no return --> win rate " + str(p2_win / 100000))
    print("draw game rate is " + str(draw_game_times / 100000))
    return p1_win / 100000, p2_win / 100000, draw_game_times / 100000

if __name__ == "__main__":
    cards_on_table = "ht_6,cl_12,dm_9"
    p1_cards = "dm_6,sp_6"
    p2_cards = "ht_13,dm_13"
    start(cards_on_table, p1_cards, p2_cards)