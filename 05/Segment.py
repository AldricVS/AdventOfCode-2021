from typing import Tuple
from Point import Point

class Segment:
    def __init__(self, point1:Point, point2:Point) -> None:
        self.point1 = point1
        self.point2 = point2
        self.is_vertical = point2.y == point1.y
        self.is_horizontal = point2.x == point1.x

    def furthest_coords(self) -> Tuple[int, int]:
        w = self.point1.x if self.point1.x > self.point2.x else self.point2.x
        h = self.point1.y if self.point1.y > self.point2.y else self.point2.y
        return (w, h)

    def left_point(self) -> Point:
        if self.point1.x < self.point2.x:
            return self.point1
        return self.point2

    def right_point(self) -> Point:
        if self.point1.x <= self.point2.x:
            return self.point2
        return self.point1