from typing import Sequence

FILE_NAME = "input.txt"
NUMBER_OF_BITS = 12

lines:Sequence[str]
with open(FILE_NAME, "r") as f:
    lines = f.readlines()

def find_wanted_bit(lines, index, search_most_common):
    count_ones = 0
    count_zeroes = 0
    for line in lines:
        if line[index] == "1":
            count_ones += 1
        else:
            count_zeroes += 1
    if search_most_common:
        return "0" if count_zeroes > count_ones else "1"
    else:
        return "1" if count_zeroes > count_ones else "0"

def find_right_line(lines, search_most_common):
    tmp_lines = lines.copy()
    index = 0
    n = ""
    while len(tmp_lines) > 1:
        wanted_bit = find_wanted_bit(tmp_lines, index, search_most_common)
        n += wanted_bit
        tmp_lines = [l for l in tmp_lines if l[index] == wanted_bit]
        index += 1
    return tmp_lines[0]

oxygen_line = find_right_line(lines, True)
co2_line = find_right_line(lines, False)

oxygen_value, co2_value = int(oxygen_line, 2), int(co2_line, 2)
print(f"Oxygen : {oxygen_value}, Co2 : {co2_value}")
print(f"So the answer is {oxygen_value * co2_value}")