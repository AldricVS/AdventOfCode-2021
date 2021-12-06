from typing import List
from Board import Board
from Point import Point
from Segment import Segment

FILE_NAME = "input.txt"

segments: List[Segment] = []
max_width, max_height = 0, 0
with open(FILE_NAME, "r") as file:
    for line in file:
        s1, s2 = line.split(" -> ")
        p1, p2 = Point.from_str(s1), Point.from_str(s2)
        seg = Segment(p1, p2)
        w, h = seg.furthest_coords()
        if max_width < w:
            max_width = w
        if max_height < h:
            max_height = h
        segments.append(seg)

board: Board = Board(max_width + 1, max_height + 1)
for segment in segments:
    board.put_segment(segment, allow_diagonals=True)

print(f"Count overlapping lines : {board.count_overlapping_lines()}")