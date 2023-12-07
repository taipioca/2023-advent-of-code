def type(hand):
    cards = {}

    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    if len(cards) == 1:
        return 7
    elif 4 in cards.values():
        return 6
    elif 3 in cards.values() and len(cards) == 2:
        return 5
    elif 3 in cards.values() and len(cards) == 3:
        return 4
    elif 2 in cards.values() and len(cards) == 3:
        return 3
    elif 2 in cards.values() and len(cards) == 4:
        return 2
    else:
        return (1)

def sort_hands(hands):
    # Define the order of the cards
    order = {'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 'T': 'e', '9': 'f', '8': 'g', '7': 'h', '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'}
    new_hands = []
    converted = []
    for hand in hands:
        current = ''
        for card in hand:
            current = current + order[card]
        new_hands.append(current)
    new_hands.sort()
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
    with open(file,'r') as info:
        for line in info:
            line = line.strip()
            cards[line.split(" ")[0]] = line.split(" ")[1]
    for i in cards.keys():
        rank[type(i)].append(i)
    
    for i in rank:
        if len(rank[i]) == 0:
            continue
        elif len(rank[i]) == 1:
            final_rank.append(rank[i][0])
        else:
            new_hands = sort_hands(rank[i])
            for j in new_hands:
                final_rank.append(j)
    total = 0
    for i in final_rank:
        total += int(cards[i])*(final_rank.index(i)+1)
    
    return total

print(camel("day_07.txt"))