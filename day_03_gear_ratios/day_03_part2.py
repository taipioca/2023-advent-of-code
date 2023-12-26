def find_num(arr, line, j):
    nums = []

    for l in range(line-1, line+2):
        for idx in range(j-1, j+1):
            num = ''
            i = idx
            while i>0 and arr[l][i].isdigit():
                i -=1
            i += 1
            while i<len(arr[l]) and arr[l][i].isdigit():
                num += (str(arr[l][i]))
                i += 1
            nums.append(num)
    return [int(i) for i in list(set(nums)) if i!= ""]

def gear(file):
    schematic = []
    gear_ratio = []
    with open(file, 'r') as puzzle_input:
        schematic = [line for line in puzzle_input]
    split = []

    for line in schematic:
        split.append(list(line))
    for line in range(len(split)):
        split[line].insert(0, '.')
        split[line].pop(len(split[line])-1)
        split[line].append('.')

    split.insert(0, ['.']*(len(split[1])-1))
    split.append(['.']*(len(split[1])-1))
    
    for line in range(1,len(split)):
        for i in range(1, len(split[line])-2):
            if split[line][i] == "*":
                if len(find_num(split, line, i)) == 2:
                    gear_ratio.append(find_num(split, line, i)[0]*find_num(split, line, i)[1])

    return sum(gear_ratio)



print(gear("day_03.txt"))
