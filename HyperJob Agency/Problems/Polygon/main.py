from abc import ABC, abstractmethod


class EquilateralPolygon(ABC):
    def __init__(self, side):
        self.side = side

    @abstractmethod
    def get_area(self):
        pass


class Square(EquilateralPolygon):
    def get_area(self):
        return self.side ** 2
