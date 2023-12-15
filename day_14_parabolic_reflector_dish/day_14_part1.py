def furthest(arr):
    for column in arr:
        for index in range(1, len(column)):
            if column[index] == "O":
                if column[index-1] == ".":
                    return False
    return True
def change(columns):
    new = columns.copy()
    for column in range(len(columns)):
        for index in range(1, len(columns[column])):
            if columns[column][index-1] == "." and columns[column][index] == "O":
                new[column][index-1] = "O"
                new[column][index] = "."
    return new

with open("day_14.txt", "r") as info:
    rows = []
    for line in info:
        list = []
        list[:] = line.strip()
        
        rows.append(list)
    columns = []
    for line in range(len(rows[0])):
        column = []
        for index in rows:
            column.append(index[line])
        columns.append(column)

new = columns.copy()
while not furthest(new):
    new = change(new)
load = []
length = len(new)

for i in range(len(new)):
    for j in range(len(new[i])):
        if new[i][j] == "O":
            load.append(length-j)
print(sum(load))
