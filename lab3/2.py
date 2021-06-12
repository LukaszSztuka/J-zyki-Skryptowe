imiona = set()
for i in range(10):
    imie = input("Podaj imie: ")
    t = False
    if imie.isalpha():
        for i in imiona:
            if i.lower() == imie:
                t = True
        if not t:
            imiona.add(imie.title())
        else:
            print("Imie w bazie")

print(imiona)