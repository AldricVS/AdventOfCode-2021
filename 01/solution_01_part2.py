
from typing import Iterator, Tuple


FILE_NAME = "input.txt"

def generate_measurements(filename) -> Iterator[Tuple[int, int, int]]:
    first, second, third = None, None, None
    with open(filename, "r") as f:
        for line in f:
            # first fill
            if first is None:
                first = int(line)
            elif second is None:
                second = int(line)
            elif third is None:
                third = int(line)
                yield (first, second, third)
            else: # we have all values
                first = second
                second = third
                third = int(line)
                yield (first, second, third)


increase_count = 0
prev_sum = 20_000_000

for values in generate_measurements(FILE_NAME):
    values_sum = sum(values)
    if values_sum > prev_sum:
        increase_count += 1
    prev_sum = values_sum

print(f"Number of increases : {increase_count}")