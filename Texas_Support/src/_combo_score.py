def _translate(combo):
    kinds_statistic = {}
    number_statistic = {}
    straight_statistic = []
    if len(combo) != 5:
        print("FATAL ERROR -> _combo_score.py: combo length is not 5")
    for card in combo:
        kinds, number = card.split("_")
        kind_times = kinds_statistic.get(kinds, 0)
        kind_times += 1
        kinds_statistic[kinds] = kind_times
        number_times = number_statistic.get(number, 0)
        number_times += 1
        number_statistic[number] = number_times
        straight_statistic.append(int(number))
    return kinds_statistic, number_statistic, straight_statistic

def is_straight(straight_statistic, number_statistic):
    sorted_combo = sorted(straight_statistic)
    if sorted_combo[-1] - sorted_combo[0] == 4 and len(number_statistic) == 5:
        return True
    if sorted_combo[-1] == 14:
        sorted_combo = sorted_combo[0:-1]
        sorted_combo.insert(0, 1)
    if sorted_combo[-1] - sorted_combo[0] == 4 and len(number_statistic) == 5:
        return True
    return False

def is_flush(kinds_statistic):
    if len(kinds_statistic) == 1:
        return True
    return False

def is_triple(number_statistic):
    counter = 0
    if len(number_statistic) == 3:
        values = number_statistic.values()
        for value in values:
            counter += value * value
    if counter == 11:
        return True
    return False

def is_two_pair(number_statistic):
    counter = 0
    if len(number_statistic) == 3:
        values = number_statistic.values()
        for value in values:
            counter += value * value
    if counter == 9:
        return True
    return False

def is_kingkong(number_statistic):
    if len(number_statistic) == 2:
        values = list(number_statistic.values())
        diff_squre = (values[0] - values[1]) * (values[0] - values[1])
        if diff_squre == 9:
            return True
    return False

def is_full_house(number_statistic):
    if len(number_statistic) == 2:
        values = list(number_statistic.values())
        diff_squre = (values[0] - values[1]) * (values[0] - values[1])
        if diff_squre == 1:
            return True
    return False

def is_one_pair(number_statistic):
    if len(number_statistic) == 4:
        return True
    return False

def calculate_rank_power(combo):
    combo_name = ""
    kinds_statistic, number_statistic, straight_statistic = _translate(combo)
    if is_flush(kinds_statistic) and is_straight(straight_statistic, number_statistic):
        rank = 9
        combo_name = "royal_flush"
    elif is_kingkong(number_statistic):
        rank = 8
        combo_name = "kingkong"
    elif is_full_house(number_statistic):
        rank = 7
        combo_name = "full_house"
    elif is_flush(kinds_statistic):
        rank = 6
        combo_name = "flush"
    elif is_straight(straight_statistic, number_statistic):
        rank = 5
        combo_name = "straight"
    elif is_triple(number_statistic):
        rank = 4
        combo_name = "triple"
    elif is_two_pair(number_statistic):
        rank = 3
        combo_name = "two_pair"
    elif is_one_pair(number_statistic):
        rank = 2
        combo_name = "one_pair"
    else:
        rank = 1
        combo_name = "high_card"
    return rank, combo_name

def calculate_kicks_power(combo, rank):
    kinds_statistic, number_statistic, straight_statistic = _translate(combo)
    kick_power = 1
    if rank == 8 or rank == 7 or rank == 3:
        for number in number_statistic:
            if number_statistic[number] >= 2:
                kick_power += 14 ** int(number) * number_statistic[number]
            else:
                kick_power += int(number)
    else:
        sorted_combo = sorted(straight_statistic, reverse = True)
        common_part_index = 5
        special_part_index = 6
        for number in sorted_combo:
            if number_statistic[str(number)] != 1:
                kick_power += 14 ** special_part_index * number
            else:
                kick_power += 14 ** common_part_index * number
                common_part_index -= 1
    if rank == 5 and 14 in straight_statistic and 2 in straight_statistic:
        # to avoid A,2,3,4,5 > 2,3,4,5,6
        kick_power = 3430489
    if rank == 9 and 14 in straight_statistic and 2 in straight_statistic:
        # to avoid A,2,3,4,5 > 2,3,4,5,6
        kick_power = 3430489
    return kick_power

if __name__ == "__main__":
    combo1 = ['ht_14', 'sp_14', 'dm_2', 'ht_4', 'cl_4', 'cl_5', 'ht_3']
    combo2 = ['cl_14', 'sp_13', 'dm_2', 'ht_4', 'cl_4', 'cl_5', 'ht_3']
    print(calculate_kicks_power(combo1, 5))
    print(calculate_kicks_power(combo2, 5))
