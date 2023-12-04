def scratchcards(file):
    win = []
    yours = []
    with open(file) as nums:
        for i in nums:
            line = i.replace("  ", " ")
            win.append((line[line.index(':')+2:line.index('|')-1]).split(" "))
            yours.append((line[line.index('|')+2:])[0:-1].split(" "))
    win_nums = [0]*len(yours)
    for game in range(len(yours)):
        win_nums[game] = len(set(win[game]) & set(yours[game]))

    for i in range(len(win_nums)):
        win_nums[i] = 2**(int(win_nums[i])-1)
        if win_nums[i] == 0.5:
            win_nums[i] = 0

        
    return sum(win_nums)
    
print(scratchcards("day_04.txt"))