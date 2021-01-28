"""
zhangyongguang
2021 01 05
"""
import _tools

def calculate_screwed_score_v2(leader_win_rate, chaser_win_rate, draw_game_rate,winner_info):
    if "chaser" in winner_info:
        screwed_score = (leader_win_rate + draw_game_rate) * 100
    if "leader" in winner_info:
        screwed_score = (chaser_win_rate + draw_game_rate / 2) * 125
    if "draw" in winner_info:
        screwed_score = (leader_win_rate - chaser_win_rate) * 100
    return screwed_score

def calculate_screwed_score_sp(win_rate_list, draw_game_rate, winner_info):
    screwed_score_list = []
    for each in win_rate_list:
        screwed_score_list.append(0)
    print("Fail to calculate")
    return screwed_score_list

def calculate_screwed_score_v1(win_rate_list, draw_game_rate, winner_info):
    screwed_score_list = []
    parts = winner_info.split("_")
    winner_index = [0] #leader win
    if "chaser" in winner_info: # 1v1 chaser win
        winner_index = [1]
    if len(parts) > 1: # 1vn chaser win
        winner_index = [int(parts[1])]
    if len(parts) > 2:
        screwed_score_list = calculate_screwed_score_sp(win_rate_list, draw_game_rate, winner_info)
        return screwed_score_list
    index = 0
    for win_rate in win_rate_list:
        if index in winner_index:
            screwed_score_list.append((1 - win_rate - draw_game_rate) * (-100))
        else:
            screwed_score_list.append(win_rate * 100)
        index += 1
    if sum(screwed_score_list) != 0:
        print("---------------warning---------------")
        print("sum screwed score is " + str(sum(screwed_score_list)))
        print(screwed_score_list)
    if "draw" in winner_info:
        screwed_score_list = []
        screwed_score = -100 * (win_rate_list[0] - sum(win_rate_list[1:]))
        for _ in range(len(win_rate_list)):
            screwed_score_list.append(screwed_score)
        screwed_score_list[0] = 100 * (win_rate_list[0] - sum(win_rate_list[1:]))
    return screwed_score_list

def update_history_score_v2(history_score, winner_info, screwed_score, leader_name, chaser_name):
    leader_score = history_score[leader_name]
    chaser_score = history_score[chaser_name]
    if "leader" in winner_info:
        leader_score -= screwed_score
        chaser_score += screwed_score
    else:
        leader_score += screwed_score
        chaser_score -= screwed_score
    history_score[leader_name] = leader_score
    history_score[chaser_name] = chaser_score
    return history_score

def update_history_score_v1(history_score, winner_info, screwed_score_list,player_name_list):
    if len(screwed_score_list) != len(player_name_list):
        print("FATAL ERROR........ the length of the player list is not eaqual to the length of teh player name list")
    index = 0
    for player_name in player_name_list:
        old_score = history_score.get(player_name, 0)
        new_score = old_score + screwed_score_list[index]
        history_score[player_name] = new_score
        index += 1
    return history_score

def info_translator_v2(leader_info, chaser_info):
    parts = leader_info.split(":")
    leader_name_code = parts[0]
    leader_name = _tools.who_is(leader_name_code)
    leader_card = parts[1]
    leader_card = _tools._card_join_convert(leader_card)
    parts = chaser_info.split(":")
    chaser_name_code = parts[0]
    chaser_name = _tools.who_is(chaser_name_code)
    chaser_card = parts[1]
    chaser_card = _tools._card_join_convert(chaser_card)
    return leader_name, chaser_name, leader_card, chaser_card

def info_translator_v1(leader_info, chaser_info_str):
    player_cards_list = []
    player_name_list = []
    parts = leader_info.split(":")
    leader_name_code = parts[0]
    leader_name = _tools.who_is(leader_name_code)
    player_name_list.append(leader_name)
    leader_card = parts[1]
    leader_card = _tools._card_join_convert(leader_card)
    player_cards_list.append(leader_card)
    chasers = chaser_info_str.split("+")
    for chaser_info in chasers:
        parts = chaser_info.split(":")
        chaser_name_code = parts[0]
        chaser_name = _tools.who_is(chaser_name_code)
        player_name_list.append(chaser_name)
        chaser_card = parts[1]
        chaser_card = _tools._card_join_convert(chaser_card)
        player_cards_list.append(chaser_card)
    return player_cards_list, player_name_list
