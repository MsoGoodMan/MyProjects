"""
zhangyongguang
2020 12 3
"""
import _card_pool_manager
import who_is_daddy
from random import *
import _tools
card_pool = {}

def start(cards_on_table, player_cards):
    global card_pool
    card_pool = _card_pool_manager.refresh_card_pool()
    table_cards = len(cards_on_table.split(","))
    if cards_on_table != "":
        card_pool = _card_pool_manager._change_card_pool(cards_on_table, "on_table", card_pool)
    else:
        table_cards = 0
    index = 1
    for player_card in player_cards:
        card_pool = _card_pool_manager._change_card_pool(player_card, "for_p" + str(index), card_pool)
        index += 1
    avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
    pad_num = 5 - table_cards
    win_times_list = [0] * len(player_cards)
    draw_game_times = 0.0
    for _ in range(100000):
        comming_card = sample(avalible_cards, pad_num)
        player_element_list = []
        for player_card in player_cards:
            player_element_list += _tools.trim_cards_for_user(cards_on_table, player_card, comming_card)
        max_combo, combo_name, rank, winner = who_is_daddy.dual(player_element_list)
        if len(winner) > 1:
            draw_game_times += 1
        else:
            win_times_list[winner[0]] += 1
    winner = 0
    for win_times in win_times_list:
        print("player" + str(winner) + " win rate " + str(win_times / 100000))
        winner += 1
    print("draw game " + str(draw_game_times / 100000))
    return win_times_list, draw_game_times

if __name__ == "__main__":
    cards_on_table = "sp_12,dm_13,cl_8,ht_9"
    p0_cards = "dm_11,sp_13"
    p1_cards = "cl_13,ht_7"
    player_cards = [p0_cards, p1_cards]
    start(cards_on_table, player_cards)