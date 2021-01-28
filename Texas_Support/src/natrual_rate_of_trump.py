"""
zhangyongguang
2020 12 14
"""
import _tools
import _card_pool_manager
import who_is_daddy
from random import *
card_pool = {}

def start(cards_on_table, my_cards, enemy_num):
    global card_pool
    card_pool = _card_pool_manager.refresh_card_pool()
    table_cards = len(cards_on_table.split(","))
    if cards_on_table != "":
        card_pool = _card_pool_manager._change_card_pool(cards_on_table, "on_table", card_pool)
    else:
        table_cards = 0
    card_pool = _card_pool_manager._change_card_pool(my_cards, "for_me", card_pool)
    avalible_cards = _card_pool_manager._get_valid_cards(card_pool)
    pad_num = 5 - table_cards
    win_times = 0.0
    draw_game_times = 0.0
    for _ in range(100000):
        sub_card_pool = card_pool.copy()
        comming_card = sample(avalible_cards, pad_num)
        sub_card_pool = (_card_pool_manager._change_card_pool(",".join(comming_card), "on_the_table", sub_card_pool))
        sub_avalible_cards = _card_pool_manager._get_valid_cards(sub_card_pool)
        player_element_list = _tools.trim_cards_for_user(cards_on_table, my_cards, comming_card)
        for index in range(enemy_num):
            player_card = sample(sub_avalible_cards, 2)
            sub_card_pool = _card_pool_manager._change_card_pool(",".join(player_card), "for_p" + str(index + 1), sub_card_pool)
            sub_avalible_cards = _card_pool_manager._get_valid_cards(sub_card_pool)
            player_element_list += _tools.trim_cards_for_user(cards_on_table, ','.join(player_card), comming_card)
        max_combo, combo_name, rank, winner = who_is_daddy.dual(player_element_list)
        if len(winner) > 1:
            draw_game_times += 1.0
        elif 0 in winner:
            win_times += 1.0
        # else:
        #     print(player_element_list)
        #     print(combo_name + "\n")
    print("Your natural trump rate is " + str(win_times / 100000))
    print("draw game rate is " + str(draw_game_times / 100000))

if __name__ == "__main__":
    cards_on_table = "dm_6,dm_14,dm_11,cl_12"
    my_cards = "dm_12,cl_10"
    start(cards_on_table, my_cards, 1)