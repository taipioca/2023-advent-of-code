import math
def next_node(instruction, nodes, current):
    if instruction == "L":
        return nodes[current][0]
    else:
        return nodes[current][1]


def haunted(file):
    nodes = {}
    starts = []
    with open(file, "r") as info:
        instructions = info.readline().strip()
        lines = info.readlines()
        for idx in range(1, len(lines)):
            nodes[lines[idx][0:3]] = [lines[idx][7:10], lines[idx][12:15]]
            if lines[idx][2] == "A":
                starts.append(lines[idx][0:3])
    nums = []
    for i in starts:
        current = i
        steps = 0
        idx = 0
        while current[2] != "Z":
            if idx == len(instructions):
                idx = 0

            current = next_node(instructions[idx], nodes, current)
            steps += 1        
            idx += 1
        nums.append(steps)
                  
    return math.lcm(*nums)

print(haunted("day_08.txt"))