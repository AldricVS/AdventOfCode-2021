from itertools import groupby, count
from typing import List
from Grid import Grid

FILE_INPUT = "input.txt"
GRID_SIZE = 5

numbers:List[int]
grids:List[Grid]
with open(FILE_INPUT, "r") as file:

    # Load numbers
    numbers = list(map(lambda s: int(s), file.readline().split(",")))
    print(numbers)
    file.readline()

    def load_grids(file, grid_size):
        all_remaining_lines = (line.rstrip() for line in file)
        all_board_lines = (line for line in all_remaining_lines if line)
        cpt = count()
        for _, one_board_lines in groupby(all_board_lines, lambda _: next(cpt) // grid_size):
            yield Grid(one_board_lines)

    # work with all grids at the same time
    grids = [grid for grid in load_grids(file, GRID_SIZE)]
    file.close()

for number in numbers:
    winners = []
    for grid in grids:
        grid.update(number)
        if grid.is_winning():
            winners.append(grid)
    if len(winners) > 0:
        break

# we should have only one winner
if len(winners) > 1:
    raise RuntimeError("Should only have one winner")
winner:Grid = winners[0]

print("Winner score : ", winner.calculate_score(number))