import math


class Vector2:
    def __init__(self,x:float, y:float, rad=False, rnd:int=4):
        self.rnd = rnd
        if rad:
            self.y = round(x * math.cos(y), rnd)
            self.x = round(x * math.sin(y), rnd)
        else:
            self.x = x
            self.y = y

    def normalize(self):
        k = math.sqrt(1/max(self.x*self.x+self.y*self.y,0.00000001))
        return self * k

    def length(self):
        return round(math.sqrt(self.x*self.x+self.y*self.y), self.rnd)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, other):
        return Vector2(self.x*other, self.y*other)

    def __truediv__(self, other):
        return self.__mul__(1.0/other)
    def __str__(self):
        return f"{self.x}|{self.y}"



class Shape2:
    _shapetypes = ["circle", "rect"]

    def __init__(self, pos, param2, type):
        if not type in Shape2._shapetypes:
            raise ValueError("Invalid Shapetype: " + type)
        self.type = type
        self.pos = pos
        self.param2 = param2

    def in_bounds(self, point):
        if self.type == "circle":
            return (self.pos - point).length() <= self.param2
        elif self.type == "rect":
            return (self.pos.x-self.param2.x/2<=point.x) and (self.pos.x+self.param2.x/2>=point.x) \
                and (self.pos.y-self.param2.y/2<=point.y) and (self.pos.y+self.param2.y/2>=point.y)


class Rect (Shape2):
    def __init__(self, pos, dim):
        self.type = "rect"
        self.pos = pos
        self.param2 = dim

class Circle (Shape2):
    def __init__(self, pos, dim):
        self.type = "circle"
        self.pos = pos
        self.param2 = dim
