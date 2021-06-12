def analiza(b):
    if b < 0:
        return -1000
    elif b == 0:
        return "ZEROOO!!!!"
    elif 0 < b < 10:
        return b
    elif 10 <= x <= 100:
        return "dużo"
    elif b > 100:
        return "bardzo duzo"


while True:
    x = input("Podaj liczbe calkowitą: ")
    x = int(x)
    print(analiza(x))
