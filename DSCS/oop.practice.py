class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def slope(self) -> float:
        if self.p1.x != self.p2.x:
            return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
        else:
            return float('inf')

    def length(self) -> float:
        return ((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)**0.5


l1 = Line(Point(1, 1), Point(2, 2))
print(l1.length())
