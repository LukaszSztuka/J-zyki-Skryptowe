def ciagF(c):
    if c == 0:
        return 0
    elif c == 1:
        return 1
    elif c > 1:
        return ciagF(c-2) + ciagF(c-1)


while True:
    x = int(input("Podaj n pierwszych wyrazow: "))
    print(ciagF(x))

