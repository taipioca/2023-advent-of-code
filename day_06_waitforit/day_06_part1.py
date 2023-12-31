def distance(time, record):
    win = 0
    for hold in range(time):
        speed = hold
        rest = time-hold
        distance = speed*rest
        if distance > record:
            win += 1
    return win


def wait(file):
    stuff = []
    with open(file, "r") as data:
        for line in data:
            stuff.append((line).strip().split(" "))
        
    times = []
    distances = []

    for i in stuff[0]:
        if i.isdigit():
            times.append(int(i))
    for i in stuff[1]:
        if i.isdigit():
            distances.append(int(i))
    product = 1
    for i in range(len(times)):
        product *= distance(times[i], distances[i])

    return product

print(wait("day_06.txt"))