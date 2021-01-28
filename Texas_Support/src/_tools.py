"""
zhangyongguang
2020 12 17
"""
def trim_cards_for_user(cards_on_table, player_cards, comming_card):
    table_cards = len(cards_on_table.split(","))
    if cards_on_table == "":
        table_cards = 0
    player_element_list = []
    if table_cards == 0:
        player_elements = (cards_on_table + player_cards).split(",") + comming_card
        player_element_list.append(player_elements)
    else:
        player_elements = (cards_on_table + ',' + player_cards).split(",") + comming_card
        player_element_list.append(player_elements)
    return player_element_list

def who_is(name_code):
    name_dict = {'hy':'韩洋', 'lxi':'李翔', 'zhh':'张翰华', 'lxu':'刘学', 'zyg':'张永光',
                 'wzc':'王子川','zwm':'章文淼','yj':'袁骏', 'jzh':'蒋志豪', 'az':'阿哲', 'ot':'局外'}
    real_name = name_dict.get(name_code, "null")
    if real_name == "null":
        print("-------------------------warning--------------------------")
        print("uknown name " + name_code)
    return real_name

def _card_join_convert(input_str):
    info_list = input_str.split("&")
    output_str = ",".join(info_list)
    return output_str

def translate_cards(input_card_str):
    if input_card_str == "null" or input_card_str == "":
        return "null"
    trans_dict = {"ht":"♥", "sp":"♠", "dm":"♦", "cl":"♣", "11":"J", "12":"Q", "13":"K", "14":"A"}
    cards_list = input_card_str.split(",")
    return_str = ""
    for card in cards_list:
        kinds, number = card.split("_")
        the_kinds = trans_dict.get(kinds, kinds)
        the_number = trans_dict.get(number, number)
        return_str += the_kinds + the_number + " "
    return return_str

def list_normolization(times_list, draw_game_times):
    new_times_list = []
    sum_score = sum(times_list) + draw_game_times
    for element in times_list:
        new_times_list.append(element / sum_score)
    draw_game_rate = draw_game_times / sum_score
    return new_times_list, draw_game_rate

if __name__ == "__main__":
    str = "dm_6,dm_14,dm_11,cl_12"
    ot = translate_cards(str)
    print(ot)
