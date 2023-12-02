def trebuchet(file):
    calibration = []
    with open(file, 'r') as calibration_doc:
        for line in calibration_doc.readlines():
            calibration.append(line)
    sum = 0
    for i in calibration:
        nums = [int(char) for char in i if char.isdigit()]
        sum += int(str(nums[0]) + str(nums[len(nums)-1]))

    return sum

print(trebuchet("day_1_part1.txt"))