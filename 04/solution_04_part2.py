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

last_winner:Grid = None
last_winning_number:int = None
for number in numbers:
    print("======")
    toRemove:List[Grid] = []
    for grid in grids:
        grid.update(number)
        if grid.is_winning():
            last_winner = grid
            last_winning_number = number
            toRemove.append(grid)
    if len(toRemove) > 0:
        grids = [g for g in grids if g not in toRemove]

print("Last winner score : ", last_winner.calculate_score(last_winning_number))