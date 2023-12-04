   
def scratchcards(file):
    win = []
    yours = []
    cards = {}
    with open(file) as nums:
        for i in nums:
            line = i.replace("  ", " ")
            win.append((line[line.index(':')+2:line.index('|')-1]).split(" "))
            yours.append((line[line.index('|')+2:])[0:-1].split(" "))
    win_nums = [0]*len(yours)
    for i in range(len(yours)):
        cards[i] = 1
    for game in range(len(yours)):
        win_nums[game] = len(set(win[game]) & set(yours[game]))

    for i in range(len(win_nums)):
        for j in range(win_nums[i]):
            if i+j < len(win_nums):
                cards[i+j+1] += cards[i]
        
    return sum(cards.values())
    
print(scratchcards("day_04.txt"))
