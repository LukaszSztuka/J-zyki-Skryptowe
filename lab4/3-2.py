from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance0(self):
        d = sqrt(pow(0 - self.x, 2) + pow(0- self.y, 2))
        print(d)

    def distance(self, a):
        d = sqrt(pow(a.x - self.x, 2)+pow(a.y - self.y, 2))
        print(d)

    def __str__(self):
        return ("Punkt (%f,%f)" % (self.x, self.y))

    def __repr__(self):
        return ("Punkt (%f,%f)" % (self.x, self.y))


class Circle(Point):
    def __init__(self, x=0, y=0, r=1):
        Point.__init__(self, x, y)
        self.r = r


p1 = Point()
p2 = Point(1, 1)
p3 = Point(2, 2)
k1 = Circle(2, 2, 1)
p3.distance(p2)
p2.distance(p3)
p3.distance0()
print(p1)
