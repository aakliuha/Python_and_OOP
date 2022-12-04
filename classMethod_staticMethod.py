class Coordinate:
    MAX_COORD = 100
    MIN_COORD = 1

    def __init__(self, x, y):
        print("init is called!")
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def getCoords(self):
        return self.x, self.y

    @classmethod
    def perimeter(cls, x, y):
        return 2*(x+y)

    @staticmethod
    def norm2(x, y):
        return x*x + y*y

v = Coordinate(5, 200)
print(v.getCoords())

print(v.norm2(1, 2))

























