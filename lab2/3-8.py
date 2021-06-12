from math import sqrt


def pier(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    if delta < 0:
        delta = -delta
        delta = sqrt(delta) * 1j
        x1 = (-b - delta) / (2 * a)
        x2 = (-b + delta) / (2 * a)
        return "Pierwiasteki wynoszą: " + str(x1) + " i " + str(x2)

    if delta >= 0:
        x1 = (-b-sqrt(delta))/(2 * a)
        if delta == 0:
            return "Pierwiastek wynosi: " + str(x1)
        else:
            x2 = (-b + sqrt(delta)) / (2 * a)
            return "Pierwiasteki wynoszą: " + str(x1) + " i " + str(x2)


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
print(pier(a, b, c))
