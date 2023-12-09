def find_difference(history):
    difference_list = []
    for val in range(len(history)-1):
        difference_list.append(int(history[val+1])-int(history[val]))
    return difference_list

def extrapolate(differences):
    value = 0
    for line in differences:
        value *= -1
        value += int(line[0])
    return value

def mirage(file):
    histories = []
    with open(file, "r") as report:
        for line in report:
            histories.append(line.strip().split(" "))
    values = []
    for history in histories:
        differences = [[int(i) for i in history]]
        difference = [int(i) for i in history]
        while not all(value == 0 for value in difference):
            differences.insert(0,find_difference(difference))
            difference = find_difference(difference)
        values.append(extrapolate(differences))

    return sum(values)

print(mirage("day_09.txt"))
    