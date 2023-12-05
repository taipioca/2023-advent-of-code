
def next_item(item, map):
    item = int(item)
    for line in map:
        if item >= int(line[1]) and item <= (int(line[1]) + int(line[2])):
            return int(line[0]) + (item-int(line[1]))
    else:
        return item

def seed(file):
    with open(file, 'r') as inputs:
        
        inputs = [line for line in inputs]
        for i in range(0,len(inputs)-1):
            inputs[i] = inputs[i][:-1]
        for i in inputs:
            if i == "\n" or len(i) == 0:
                inputs.pop(inputs.index(i))

            
    seeds = inputs[0][7:].split(" ")
    seeds_soil = inputs[inputs.index("seed-to-soil map:")+1: inputs.index("soil-to-fertilizer map:")]
    for i in range(len(seeds_soil)):
        seeds_soil[i] = seeds_soil[i].split(" ")
    soil_fert = inputs[inputs.index("soil-to-fertilizer map:")+1:inputs.index("fertilizer-to-water map:")]
    for i in range(len(soil_fert)):
        soil_fert[i] = soil_fert[i].split(" ")
    fert_water = inputs[inputs.index("fertilizer-to-water map:")+1:inputs.index("water-to-light map:")]
    for i in range(len(fert_water)):
        fert_water[i] = fert_water[i].split(" ")
    water_light = inputs[inputs.index("water-to-light map:")+1:inputs.index("light-to-temperature map:")]
    for i in range(len(water_light)):
        water_light[i] = water_light[i].split(" ")
    light_temp = inputs[inputs.index("light-to-temperature map:")+1:inputs.index("temperature-to-humidity map:")]
    for i in range(len(light_temp)):
        light_temp[i] = light_temp[i].split(" ")
    temp_hum = inputs[inputs.index("temperature-to-humidity map:")+1:inputs.index("humidity-to-location map:")]
    for i in range(len(temp_hum)):
        temp_hum[i] = temp_hum[i].split(" ")
    hum_loc = inputs[inputs.index("humidity-to-location map:")+1:]
    for i in range(len(hum_loc)):
        hum_loc[i] = hum_loc[i].split(" ")


    locations = []

    for seed in seeds:
        soil = next_item(int(seed), seeds_soil)
        fert = next_item(int(soil), soil_fert)
        water = next_item(int(fert), fert_water)
        light = next_item(int(water), water_light)
        temp = next_item(int(light), light_temp)
        hum = next_item(int(temp), temp_hum)
        loc = next_item(int(hum), hum_loc)


        locations.append(loc)

    return min(locations)        


print(seed("day_05.txt"))