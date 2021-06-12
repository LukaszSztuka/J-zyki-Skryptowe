imiona = set()
lista = []
while True:
    imie = input("Podaj imie: ")
    if imie.lower() != "koniec":
        if imie.isalpha():
            imiona.add(imie.title())

    else:
        lista = sorted(imiona)
        with open("imiona.txt", 'w') as f:
            for i in lista:
                f.write(i + "\n")
        break

print(lista)
