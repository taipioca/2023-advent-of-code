# create rows and columns from input
rows = []
with open("day_11.txt", "r") as info:
    for line in info:
        rows.append(line.strip())
columns = ['']*len(rows[0])
for row in range(len(rows)):
    for pos in range(len(rows[0])):
        columns[pos] += (rows[row][pos])

# figure out which rows are empty: space only
space_rows = []
for line in range(len(rows)):
    if "#" not in rows[line]:
        space_rows.append(line)
space_columns = []
for line in range(len(columns)):
    if "#" not in columns[line]:
        space_columns.append(line)

# insert an additional "empty" row and column each time it shows up
empty = "."*len(rows[0])

x = 0
for i in range(len(space_rows)):
    space_rows[i] += x
    rows.insert(space_rows[i], empty)
    x += 1

x = 0
for i in range(len(space_columns)):
    space_columns[i] += x
    for j in range(len(rows)):
        rows[j] = rows[j][:space_columns[i]] + "." + rows[j][space_columns[i]:]
    x += 1

# store galaxies and their positions in a dictionary
galaxies = {}
num = 1
for x in range(len(rows)):
    for y in range(len(rows[x])):
        if rows[x][y] == "#":
            galaxies[num] = (x,y)
            num += 1

# generate all galaxy pairs
pairs = []
for i in range(1, len(galaxies)+1):
    for j in range(i+1, len(galaxies)+1):
        pairs.append((i, j))

# add together deltax and deltay dimensions of pairs
products = 0
for pair in pairs:
    x1 = galaxies[pair[0]][0]
    x2 = galaxies[pair[1]][0]
    y1 = galaxies[pair[0]][1]
    y2 = galaxies[pair[1]][1]

    products += (abs(x2-x1)+abs(y2-y1))

print(products)