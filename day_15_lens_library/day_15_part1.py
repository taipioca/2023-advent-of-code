# ord("char") --> gives ascii character

def poop(current, val):
    new = current
    new = ((new + ord(val))*17)%256
    return new

with open("day_15.txt", "r") as info:
    sequences = info.read().split(",")

results = []
for sequence in sequences:
    seq_sum = 0
    for char in range(len(sequence)):
        seq_sum = poop(seq_sum, sequence[char])
    results.append(seq_sum)

print(sum(results))