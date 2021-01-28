"""
zhangyongguang
2020 11 2
"""
card_pool = {}
def _shuffle_cards(kind):
    for i in range(13):
        height = str(i + 2)
        card_id = kind + height
        card_pool[card_id] = "hide_in"
    return

def refresh_card_pool():
    global card_pool
    kinds = ["ht_", "sp_", "cl_", "dm_"]
    usage = map(_shuffle_cards, kinds)
    list(usage)
    return card_pool

def _get_valid_cards(card_pool):
    avalible_cards = []
    for card in card_pool:
        card_status = card_pool[card]
        if card_status == "hide_in":
            avalible_cards.append(card)
    return avalible_cards

def _change_card_pool(cards, keywords, card_pool):
    card_list = cards.split(",")
    for card in card_list:
        status = card_pool.get(card, "not_found")
        if status == "not found":
            print("-------------warning----------")
            print("cards not found\t" + card)
            return False
        if status != "hide_in":
            print("-------------warning----------")
            print("find a weird card\t" + card)
            return False
        status = keywords
        card_pool[card] = status
    return card_pool