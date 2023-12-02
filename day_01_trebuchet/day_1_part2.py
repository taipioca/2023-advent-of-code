def has_words(line):
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for j in words:
        if j in line:
            return True
    return False

def replace(file):
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    words_pos = {}
    calibration = []
    new = []

    with open(file, 'r') as calibration_doc:
        for line in calibration_doc.readlines():
            calibration.append(line)
    for line in range(len(calibration)):
        current = calibration[line]
        while has_words(current):
            words_pos = {}
            for j in words:
                if j in current:
                    words_pos[current.index(j)] = j               
            first_word = words_pos[min(words_pos)]
            current = current.replace(first_word, first_word[0] + str(words.index(first_word))+first_word[1:])
        new.append(current)

    return new


def trebuchet(file):
    sum = 0
    for i in file:
        nums = [int(char) for char in i if char.isdigit()]
        sum += int(str(nums[0]) + str(nums[len(nums)-1]))

    return sum

print(trebuchet(replace("day_1_part2.txt")))