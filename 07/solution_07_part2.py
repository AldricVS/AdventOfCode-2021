from typing import List
from pathlib import Path
import sys

FILE_INPUT = "input.txt"

def fuel_sum(distance):
    return sum(i for i in range(1, distance + 1))

positions:List[int] = [int(s) for s in Path(FILE_INPUT).read_text().split(",")]
positions.sort()

min_pos, max_pos = min(positions), max(positions)
min_fuel = sys.maxsize

print(f"Go from {min_pos} to {max_pos}")
for i in range(min_pos, max_pos + 1):
    fuel = sum(fuel_sum(abs(i - n)) for n in positions)
    min_fuel = min(min_fuel, fuel)

print("Result :", min_fuel)