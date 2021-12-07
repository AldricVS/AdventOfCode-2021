from typing import List

FILE_INPUT = "input.txt"
NUMBER_OF_DAYS = 256

lanternfishs_per_timer = {l: 0 for l in range(10)}
lanternfishs:List[int]
with open(FILE_INPUT, "r") as f:
    strings = f.readline().split(",")
    lanternfishs = [int(s) for s in strings]
for l in lanternfishs:
    lanternfishs_per_timer[l] += 1

for day in range(1, NUMBER_OF_DAYS + 1):
    l0_count = lanternfishs_per_timer[0]
    for index in range(1, len(lanternfishs_per_timer)):
        lanternfishs_per_timer[index - 1] = lanternfishs_per_timer[index]
    lanternfishs_per_timer[6] += l0_count
    lanternfishs_per_timer[8] += l0_count

print(f"After {NUMBER_OF_DAYS} days, we have {sum(v for v in lanternfishs_per_timer.values())} lanternfishs")
