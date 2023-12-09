def next_node(instruction, nodes, current):
    if instruction == "L":
        return nodes[current][0]
    else:
        return nodes[current][1]


def haunted(file):
    nodes = {}
    with open(file, "r") as info:
        instructions = info.readline().strip()
        lines = info.readlines()
        for idx in range(1, len(lines)):
            nodes[lines[idx][0:3]] = [lines[idx][7:10], lines[idx][12:15]]
    current = "AAA"
    idx = 0
    steps = 0

    while current != "ZZZ":
        if idx == len(instructions):
            idx = 0

        current = next_node(instructions[idx], nodes, current)
        steps += 1        
        idx += 1
         
    return steps

print(haunted("day_08.txt"))