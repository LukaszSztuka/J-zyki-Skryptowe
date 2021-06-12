while True:
    x = input("Podaj liczbe calkowitą: ")
    x = int(x)

    if x < 0:
        print(-1000)
    elif x == 0:
        print("ZEROOO!!!!")
    elif 0 < x < 10:
        print(x)
    elif 10 <= x <= 100:
        print("dużo")
    elif x > 100:
        print("bardzo duzo")