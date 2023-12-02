def cube(file):
    games = {} # game id: [max r,max g,max b]
    game_id = 1
    max_red = 12
    max_green = 13
    max_blue = 14

    with open(file, 'r') as game_list:
        for line in game_list:
            game = line.split(";")
            red = []
            green = []
            blue= []
            for i in game:
                i = i.replace(",", "")
                game_pull = i.split()
                print(i)
                red.append(sum([int(game_pull[i-1]) for i in range(len(game_pull)) if game_pull[i] == "red"]))
                green.append(sum([int(game_pull[i-1]) for i in range(len(game_pull)) if game_pull[i] == "green"]))
                blue.append(sum([int(game_pull[i-1]) for i in range(len(game_pull)) if game_pull[i] == "blue"]))

            if red ==[]:
                red = [0]
            if green == []:
                green = [0]
            if blue == []:
                blue = [0]

            games[game_id] = [sorted(red, reverse = True), sorted(green, reverse = True), sorted(blue, reverse = True)]
            print(games[game_id])
            game_id += 1


    possible = []
    for id in games:
        if games[id][0][0] <= max_red and games[id][1][0] <= max_green and games[id][2][0] <= max_blue:
            possible.append(id)
    return sum(possible)

print(cube("day_2_part2.txt"))


