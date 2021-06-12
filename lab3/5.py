import pickle

imiona = set()
imionaM = set()
imionaD = set()
lista = []
listaM = []
listaD = []

with open("imiona.txt", 'r') as f:
    for line in f:
        imiona.add(line.rstrip('\n'))

while True:
    imie = input("Podaj imie: ")
    imie = imie.lower()
    if imie != "koniec":
        if imie.isalpha():
            if (imie == 'kosma' or imie == 'barnaba' or imie == 'bonawentura' or imie == 'jarema' or imie == 'kuba') or (not imie.endswith('a')):
                imiona.add(imie.title())
                imionaM.add(imie.title())
            else:
                imiona.add(imie.title())
                imionaD.add(imie.title())
                

    else:
        lista = sorted(imiona)
        listaM = sorted(imionaM)
        listaD = sorted(imionaD)
        with open("imiona.txt", 'w') as f:
            for i in lista:
                f.write(i + "\n")

        pickle.dump(listaM, open( "imionaMeskie.p", "wb" ) )
        pickle.dump(listaD, open( "imionaDamskie.p", "wb" ) )
        break

print(imionaM)
print(imionaD)
