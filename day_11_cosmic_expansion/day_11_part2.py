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

# create dictionary of each galaxy and their coordinates
galaxies = {}
num = 1
for x in range(len(rows)):
    for y in range(len(rows[x])):
        if rows[x][y] == "#":
            galaxies[num] = (x,y)
            num += 1

# set each galaxy to its new coordinates by comparing its position to the empty rows and columns. 
# depending on how many empty rows/columns it is after, add that many * a million to its row or column coordinate
new_rows = space_rows
new_columns = space_columns
new_galaxies = {}
for galaxy in galaxies:    
    new_rows.append(galaxies[galaxy][0])
    new_rows = sorted(new_rows)

    new_columns.append(galaxies[galaxy][1])
    new_columns = sorted(new_columns)

    x_pos = new_rows.index(galaxies[galaxy][0]) 
    y_pos = new_columns.index(galaxies[galaxy][1]) 
    new_galaxies[galaxy] = (galaxies[galaxy][0] + (x_pos*999999), galaxies[galaxy][1] + (y_pos*999999))
    new_rows.remove(galaxies[galaxy][0])
    new_columns.remove(galaxies[galaxy][1])

# generate all galaxy pairs
pairs = []
for i in range(1, len(new_galaxies)+1):
    for j in range(i+1, len(new_galaxies)+1):
        pairs.append((i, j))

# find shortest distance by adding deltax + deltay
products = 0
for pair in pairs:
    x1 = new_galaxies[pair[0]][0]
    x2 = new_galaxies[pair[1]][0]
    y1 = new_galaxies[pair[0]][1]
    y2 = new_galaxies[pair[1]][1]

    products += (abs(x2-x1)+abs(y2-y1))
    

print(products)