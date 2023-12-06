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
            stuff.append((line).strip())
        
    times = ''
    distances = ''

    for i in stuff[0]:
        if i.isdigit():
            times = times + i
    for i in stuff[1]:
        if i.isdigit():
            distances = distances + i
    times = int(times)
    distances = int(distances)
    print(times)
    print(distances)

    product = distance(times, distances)

    return product

print(wait("day_06.txt"))