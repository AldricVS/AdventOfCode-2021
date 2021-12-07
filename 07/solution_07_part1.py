from typing import List
from pathlib import Path

FILE_INPUT = "input.txt"

positions:List[int] = [int(s) for s in Path(FILE_INPUT).read_text().split(",")]
positions.sort()

target = positions[len(positions) // 2]
res = sum(abs(target - n) for n in positions)
print(res)