from typing import List

DEBUG = False
FILE_INPUT = "test.txt"
NUMBER_OF_DAYS = 80

lanternfishs:List[int]
with open(FILE_INPUT, "r") as f:
    strings = f.readline().split(",")
    lanternfishs = [int(s) for s in strings]

def display_lanternfishs(lanternfishs, day = 0):
    str_list = [str(i) for i in lanternfishs]
    print(f"After day {day}\t: {','.join(str_list)}")


if DEBUG: display_lanternfishs(lanternfishs)
for day in range(1, NUMBER_OF_DAYS + 1):
    for index in range(len(lanternfishs)):
        if lanternfishs[index] == 0:
            lanternfishs[index] = 6
            lanternfishs.append(8)
        else:
            lanternfishs[index] -= 1
    if DEBUG: display_lanternfishs(lanternfishs, day)

print(f"After {NUMBER_OF_DAYS} days, we have {len(lanternfishs)} lanternfishs")
