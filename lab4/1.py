from math import sqrt, hypot


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance0(self):
        print(hypot(self.x, self.y))

    def distance(self, a):
        d = sqrt(pow(a.x - self.x, 2)+pow(a.y - self.y, 2))
        print(d)

    def __str__(self):
        return ("Punkt (%f,%f)" % (self.x, self.y))

    def __repr__(self):
        return ("Punkt (%f,%f)" % (self.x, self.y))


p1 = Point()
p2 = Point(1, 1)
p3 = Point(2, 2)
p3.distance(p2)
p2.distance(p3)
p3.distance0()
print(p1)
print(p2)
