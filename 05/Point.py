
class Point:
    def __init__(self, x, y) -> None:
        self.x:int = x
        self.y:int = y

    @staticmethod
    def from_str(str) -> "Point":
        x, y = str.split(",")
        return Point(int(x), int(y))