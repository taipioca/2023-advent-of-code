def is_part_number(arr, line, last, first):
    symbol = ["*", "#", "+", '$', "*", "%" ,"/", "@", "=", "-", "&"]
    for index in range(first-1, last+2):
        if arr[line-1][index] in symbol or arr[line+1][index] in symbol or arr[line][index] in symbol:
            return True
    return False

def gear(file):
    schematic = []
    part_number = []
    with open(file, 'r') as puzzle_input:
        schematic = [line for line in puzzle_input]
    split = []

    for line in schematic:
        split.append(list(line))
    for line in range(len(split)-1):
        split[line].insert(0, '.')
        split[line].pop(len(split[line])-1)
        split[line].append('.')

    split.insert(0, ['.']*(len(split[1])-1))
    split.append(['.']*(len(split[1])-1))
    part_number = []

    for line in range(len(split)):
        num = ''
        num_indices = []
        for i in range(len(split[line])):
            if split[line][i].isdigit():
                num_indices.append(i)
                num += str(split[line][i])
                if split[line][i+1].isdigit():
                    continue
                else:
                    if is_part_number(split, line, num_indices[-1], num_indices[0]):
                        part_number.append(int(num))
                num = ''
                num_indices = []
    return sum(part_number)


print(gear("day_03.txt"))