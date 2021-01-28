# -*- coding:utf-8 -*-
import about_screwed_score
import all_in_1v1_twice
import all_in_before_river
import _tools

def load_history_record():
    path = "../data/output/screwed_score1218.csv"
    f = open(path, "r")
    lines = f.readlines()
    history_score = {}
    for line in lines:
        parts = line.strip().split(",")
        player_name = parts[0]
        score = parts[1]
        history_score[player_name] = float(score)
    f.close()
    print("start.................load history record")
    #print(history_score)
    return history_score

def write_down_process_v2(cards_on_table,leader_name, chaser_name, leader_win_rate, chaser_win_rate,
                          winner_info, leader_card, chaser_card, screwed_score, draw_game_rate, record_date):
    f = open("../data/output/record.txt", "a", encoding="utf8")
    content = "♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ " + record_date + " ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ \n"
    public_cards = _tools.translate_cards(cards_on_table)
    content += "公牌： " + public_cards + "\n"
    leader_cards = _tools.translate_cards(leader_card)
    content += "领先： " + leader_name + "->" + leader_cards + " 领先方胜率：" + str(leader_win_rate) + "\n"
    chaser_cards = _tools.translate_cards(chaser_card)
    content += "追牌： " + chaser_name + "->" + chaser_cards + " 追牌方胜率：" + str(chaser_win_rate) + "\n"
    content += "模式：两轮   平分概率： " + str(draw_game_rate) + "\n"
    if "leader" in winner_info:
        content += "结果： " + leader_name + " 两次领先获胜\n"
        content += "悲惨指数 = (追牌方胜率 + 平分概率 * 0.5) * 125 = " + str(screwed_score) + "\n"
        content += "影响：" + leader_name + " -" + str(screwed_score) + "  " + chaser_name + " +" + str(screwed_score) + "\n"
    if "chaser" in winner_info:
        content += "结果： " + chaser_name + " 两次反超获胜\n"
        content += "悲惨指数 = (领先方胜率 + 平分概率) * 100 = " + str(screwed_score) + "\n"
        content += "影响：" + leader_name + " +" + str(screwed_score) + "  " + chaser_name + " -" + str(screwed_score) + "\n"
    if "draw" in winner_info:
        content += "结果： " + leader_name + "," + chaser_name + " 平分底池\n"
        content += "悲惨指数 = (领先方胜率 - 追牌方胜率) * 100 = " + str(screwed_score) + "\n"
        content += "影响：" + leader_name + " +" + str(screwed_score) + "  " + chaser_name + " -" + str(screwed_score) + "\n"
    content += "\n\n"
    print(content)
    f.write(content)
    f.close()
    return

def write_down_process_v1(cards_on_table, player_name_list, win_rate_list, winner_info, player_cards_list, screwed_score_list, draw_game_rate, record_date):
    f = open("../data/output/record.txt", "a", encoding="utf8")
    leader_name = player_name_list[0]
    leader_screwed_score = screwed_score_list[0]
    content = "♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ " + record_date + " ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ \n"
    public_cards = _tools.translate_cards(cards_on_table)
    content += "公牌： " + public_cards + "\n"
    leader_cards = _tools.translate_cards(player_cards_list[0])
    content += "领先： " + leader_name + "->" + leader_cards + " 领先方胜率：" + str(win_rate_list[0]) + "\n"
    index = 0
    for chaser_name in player_name_list:
        if index == 0:
            index += 1
            continue
        chaser_card = player_cards_list[index]
        chaser_win_rate = win_rate_list[index]
        index += 1
        chaser_cards = _tools.translate_cards(chaser_card)
        content += "追牌： " + chaser_name + "->" + chaser_cards + " 追牌方胜率：" + str(chaser_win_rate) + "\n"
    content += "模式：一轮   平分概率： " + str(draw_game_rate) + "\n"
    if "leader" in winner_info:
        content += "结果： " + leader_name + " 持续领先获胜\n"
        content += "悲惨指数 = 追牌方胜率 * 100 = " + str(sum(screwed_score_list[1:])) + "\n"
        content += "影响：" + leader_name + " -" + str(sum(screwed_score_list[1:]))
    if "chaser" in winner_info:
        content += "结果： " + chaser_name + " BB反超获胜\n"
        content += "悲惨指数 = 领先方胜率 * 100 = " + str(leader_screwed_score) + "\n"
        content += "影响：" + leader_name + " +" + str(leader_screwed_score)
    if "draw" in winner_info:
        content += "结果： " + leader_name + "," + chaser_name + " 平分底池\n"
        content += "悲惨指数 = (领先方胜率 - 追牌方胜率) * 100 = " + str(leader_screwed_score) + "\n"
        content += "影响：" + leader_name + " +" + str(leader_screwed_score)
    index = 0
    for chaser_name in player_name_list:
        if index == 0:
            index += 1
            continue
        if screwed_score_list[index] > 0:
            content += "  " + chaser_name + " +" + str(screwed_score_list[index])
        else:
            content += "  " + chaser_name + " " + str(screwed_score_list[index])
        index += 1
    content += "\n\n"
    print(content)
    f.write(content)
    f.close()
    return

def twice_processor(leader_info, chaser_info, cards_on_table, winner_info, history_score, record_date):
    leader_name, chaser_name, leader_card, chaser_card = about_screwed_score.info_translator_v2(leader_info, chaser_info)
    leader_win_rate, chaser_win_rate, draw_game_rate = all_in_1v1_twice.start(cards_on_table, leader_card, chaser_card)
    screwed_score = about_screwed_score.calculate_screwed_score_v2(leader_win_rate, chaser_win_rate,draw_game_rate, winner_info)
    new_history_score = about_screwed_score.update_history_score_v2(history_score, winner_info, screwed_score, leader_name, chaser_name)
    write_down_process_v2(cards_on_table, leader_name, chaser_name, leader_win_rate, chaser_win_rate,winner_info, leader_card, chaser_card, screwed_score, draw_game_rate, record_date)
    return new_history_score

def once_processor(leader_info, chaser_info, cards_on_table, winner_info, history_score, record_date):
    player_cards_list, player_name_list = about_screwed_score.info_translator_v1(leader_info, chaser_info)
    win_times_list, draw_game_times = all_in_before_river.start(cards_on_table, player_cards_list)
    win_rate_list, draw_game_rate = _tools.list_normolization(win_times_list, draw_game_times)
    screwed_score_list = about_screwed_score.calculate_screwed_score_v1(win_rate_list, draw_game_rate, winner_info)
    new_history_score = about_screwed_score.update_history_score_v1(history_score, winner_info, screwed_score_list,player_name_list)
    write_down_process_v1(cards_on_table, player_name_list, win_rate_list, winner_info, player_cards_list, screwed_score_list, draw_game_rate, record_date)
    return new_history_score

def start_calculation(history_score, game_date, input_path):
    f = open(input_path, "r")
    lines = f.readlines()[1:]
    for line in lines:
        parts = line.strip().split(",")
        leader_info = parts[0]
        chaser_info = parts[1]
        public_info = parts[2]
        winner_info = parts[3]
        record_date = parts[4]
        # if record_date != game_date:
        #     continue
        if public_info == "null":
            cards_on_table = ""
        else:
            cards_on_table = _tools._card_join_convert(public_info)
        if "twice" in winner_info:
            print(line.strip())
            new_history_score = twice_processor(leader_info, chaser_info, cards_on_table, winner_info, history_score, record_date)
            print(new_history_score)
        else:
            print(line.strip())
            new_history_score = once_processor(leader_info, chaser_info, cards_on_table, winner_info, history_score, record_date)
            print(new_history_score)
    f.close()
    print(new_history_score)
    print("-----------------------------------------------------")
    return new_history_score

def output_screwed_score(new_history_score, game_date):
    f = open("../data/output/screwed_score" + game_date + ".csv", "w")
    for name in new_history_score:
        content = name + "," + str(new_history_score[name]) + "\n"
        f.write(content)
    f.close()
    return

if __name__ == "__main__":
    history_score = load_history_record()
    input_path = "../data/input/input.csv"
    game_date = "20210116"
    new_history_score = start_calculation(history_score, game_date, input_path)
    output_screwed_score(new_history_score, game_date)