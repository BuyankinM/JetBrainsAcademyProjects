class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def dist(self, point_b):
        return ((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2) ** 0.5