# ord("char") --> gives ascii character

def poop(current, val):
    new = current
    new = ((new + ord(val))*17)%256
    return new

with open("day_15.txt", "r") as info:
    sequences = info.read().split(",")

labels = {}
for sequence in sequences:
    seq_sum = 0
    for char in range(len(sequence)):
        if sequence[char] == "=":
            operation = sequence[char]
            lens = [sequence[:char],sequence[char + 1:]]
            break
        if sequence[char] == "-":
            operation = sequence[char]
            lens = [sequence[:char],0]
            break
        seq_sum = poop(seq_sum, sequence[char])
    seq_sum += 1

    if operation == "-":
        if seq_sum in labels:
            x = next((i for i, sub_array in enumerate(labels[seq_sum]) if sub_array[0] == lens[0]), -1)
            if x != -1:
                labels[seq_sum].pop(x)
    else:
        if seq_sum not in labels:
            labels[seq_sum] = [lens]
        else:
            x = next((i for i, sub_array in enumerate(labels[seq_sum]) if sub_array[0] == lens[0]), -1)
            if x == -1:
                labels[seq_sum].append(lens)
            else:
                labels[seq_sum][x] = lens

focusing_power = []
for box in labels:
    for lens in range(len(labels[box])):
        focusing_power.append(box*(lens+1)*int(labels[box][lens][1]))

print(sum(focusing_power))