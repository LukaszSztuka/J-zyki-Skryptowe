imiona = set()
lista = []

with open("imiona.txt", 'r') as f:
    for line in f:
        imiona.add(line.rstrip('\n'))

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
