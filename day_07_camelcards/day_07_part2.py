def type(hand):
    cards = {}
    # frequency of each card type in the hand
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1

    if "J" in cards and hand.count("J") != 5:
        highest_card = max(set(hand.replace("J", "")), key = hand.count)
        cards[highest_card] += cards["J"]
        cards.pop("J")

    # figure out type of hand
    if len(cards) == 1:
        return 7 # five of a kind
    elif 4 in cards.values():
        return 6 # four of a kind
    elif 3 in cards.values() and len(cards) == 2:
        return 5 # full house
    elif 3 in cards.values() and len(cards) == 3:
        return 4 # three of a kind
    elif 2 in cards.values() and len(cards) == 3:
        return 3 # two pair
    elif 2 in cards.values() and len(cards) == 4:
        return 2 # one pair
    else:
        return 1 # high card

def sort_hands(hands):
    # define order of the cards
    order = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'n', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'}
    new_hands = []
    converted = []

    # convert to letters for easier sorting
    for hand in hands:
        current = ''
        for card in hand:
            current = current + order[card]
        new_hands.append(current)
    new_hands.sort()

    # convert back to hands
    for hand in new_hands:
        current = ''
        for card in hand:
            current = current + list(filter(lambda x: order[x] == card, order))[0]
        converted.insert(0,current)
    
    return converted


def camel(file):
    cards = {}
    rank = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    final_rank = []

    # categorize all hands into types
    with open(file,'r') as info:
        for line in info:
            line = line.strip()
            cards[line.split(" ")[0]] = line.split(" ")[1]
    for i in cards.keys():
        rank[type(i)].append(i)
    
    # if multiple of a type, rank based on sorting algorithm and add back in
    for i in rank:
        if len(rank[i]) == 0:
            continue
        elif len(rank[i]) == 1:
            final_rank.append(rank[i][0])
        else:
            new_hands = sort_hands(rank[i])
            for j in new_hands:
                final_rank.append(j)
    
    # calculate winnings
    total = 0
    for i in final_rank:
        total += int(cards[i])*(final_rank.index(i)+1)
    
    return total

print(camel("day_07.txt"))