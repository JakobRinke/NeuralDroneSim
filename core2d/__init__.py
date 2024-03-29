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
        if self.length() == 0:
            return Vector2(0, 0)
        k = math.sqrt(1/(self.x*self.x+self.y*self.y))
        return round(self * k, self.rnd)

    def __round__(self, n=None):
        return Vector2(round(self.x, n), round(self.y, n))


    def to_tuple(self):
        return (self.x, self.y)

    def length(self):
        return round(math.sqrt(self.x*self.x+self.y*self.y), self.rnd)

    def inverse_Y(self):
        return Vector2(self.x, -self.y)

    def inverse_(self):
        return Vector2(-self.x, self.y)

    def as_rad_tuple(self):
        return (self.length(), math.asin(self.normalize().x))

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

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __pow__(self, power, modulo=None):
        return Vector2(self.x**power, self.y**power)


Vector2_zero = Vector2(0, 0)
Vector2_one = Vector2(1, 1)
Vector2_right = Vector2(0, 1)
Vector2_up = Vector2(1, 0)


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

    def in_bounds(self, point):
        return (self.pos.x-self.param2.x/2<=point.x) and (self.pos.x+self.param2.x/2>=point.x) \
            and (self.pos.y-self.param2.y/2<=point.y) and (self.pos.y+self.param2.y/2>=point.y)

class Circle (Shape2):
    def __init__(self, pos, dim):
        self.type = "circle"
        self.pos = pos
        self.param2 = dim

    def in_bounds(self, point):
        return (self.pos - point).length() <= self.param2