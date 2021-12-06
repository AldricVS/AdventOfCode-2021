from Segment import Segment
from Point import Point

class Board:
    def __init__(self, width, height) -> None:
        self.data = [[0 for col in range(width)] for row in range(height)]
        self.width = width
        self.height = height

    def put_segment(self, segment:Segment, allow_diagonals:bool=False) -> None:
        p1, p2 = segment.point1, segment.point2
        if segment.is_vertical:
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                self.data[p1.y][x] += 1
        elif segment.is_horizontal:
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                self.data[y][p1.x] += 1
        elif allow_diagonals:
            left_point = segment.left_point()
            right_point = segment.right_point()
            y_delta = 1 if left_point.y < right_point.y else -1
            y = left_point.y
            for x in range(left_point.x, right_point.x + 1):
                self.data[y][x] += 1
                y += y_delta

        else:
            raise RuntimeError("Unexpected event")

    def count_overlapping_lines(self) -> int:
        return sum(1 for line in self.data for elt in line if elt > 1)