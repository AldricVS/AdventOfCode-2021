
from typing import List

class Grid:
    def __init__(self, data_str:List[str]) -> None:
        data_list = [line.split() for line in data_str]
        self._data = [[int(s) for s in line] for line in data_list]
        self._data_size = len(self._data)
        self._marked = [[False for i in range(self._data_size)] for j in range(self._data_size)]
        self._positions = {self._data[x][y]: (x, y) for x in range(self._data_size) for y in range(self._data_size)}
        self._bingos = {
            "lines": [0] * self._data_size,
            "cols": [0] * self._data_size,
            "diagonals": [0, 0]
        }
    
    def update(self, val):
        line, col = self._positions.get(val, (None, None))
        if line is None:
            return
        self._marked[line][col] = True
        self._bingos["lines"][line] += 1
        self._bingos["cols"][col] += 1
        if line == col:
            if line == 2:
                self._bingos["diagonals"][1] += 1
            self._bingos["diagonals"][0] += 1
        elif line + col == 4:
            self._bingos["diagonals"][1] += 1

    def is_winning(self):
        return self._data_size in self._bingos["lines"] \
            or self._data_size in self._bingos["cols"] \
            or self._data_size in self._bingos["diagonals"]

    def calculate_score(self, last_number:int) -> int:
        size = self._data_size
        unmarked = (self._data[x][y] for x in range(size) for y in range(size) if not self._marked[x][y])
        return sum(unmarked) * last_number