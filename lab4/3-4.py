from math import sqrt, pi


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

    def circumference(self):
        return 2*pi*self.r

    def area(self):
        return pi*self.r*self.r

    def move(self, point):
        self.x = self.x + point[0]
        self.y = self.y + point[1]

    def __str__(self):
        return ("Środek (%f,%f), promień: %f" % (self.x, self.y, self.r))

    def __repr__(self):
        return ("Środek (%f,%f), promień: %f" % (self.x, self.y, self.r))


p1 = Point()
p2 = Point(1, 1)
p3 = Point(2, 2)
k1 = Circle(2, 0, 1)
p3.distance(p2)
p3.distance0()
print(k1.area())
print(k1.circumference())
print(p1)
print(k1)

k1.move((1, 2))
print(k1)

k1.move([-1, -1])
print(k1)
