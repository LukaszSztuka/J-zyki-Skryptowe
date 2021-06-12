"""1
slownik = {"1":"jeden","2":"dwa","3":"trzu","4":"cztery","5":"pięć","6":"sześć","7":"siedem","8":"osiem","9":"dziewięć","0":"zero",}
x = input("Podaj cyfre ")
print("Twoja cyfra to "+ slownik.get(x))
"""

"""2
def sprawdz(imie):
    poprawne = 0
    for litera in imie:
        if (litera.isalpha() == False):
            print("Imiona nie zawierają cyfr")
            return 0
        else:
            poprawne+=1
    if poprawne == len(imie):
        return 1
            
    
lista=[]
iterator = 0
while (iterator < 10):
    imie = input("Podaj imie: ")
    imie = imie.capitalize()
    if (sprawdz(imie) == 1):
        if imie in lista:
            print("Podano już to imie")
        else:
            lista.append(imie)
            iterator +=1
print(lista)
"""

"""3
def sprawdz(imie):
    poprawne = 0
    for litera in imie:
        if (litera.isalpha() == False):
            print("Imiona nie zawierają cyfr")
            return 0
        else:
            poprawne+=1
    if poprawne == len(imie):
        return 1
            
    
lista=[]
iterator = 0
koniec = 0
while (koniec!=1):
    imie = input("Podaj imie: ")
    imie = imie.capitalize()
    if (imie == "Koniec"):
        koniec = 1
    if (sprawdz(imie) == 1 and imie!="Koniec"):
        if imie in lista:
            print("Podano już to imie")
        else:
            lista.append(imie)
            iterator +=1
lista.sort()
plik = open("imiona.txt","w+")
for i in lista:
    plik.write("%s\n" % i)
plik.close()
"""

"""4
def sprawdz(imie):
    poprawne = 0
    for litera in imie:
        if (litera.isalpha() == False):
            print("Imiona nie zawierają cyfr")
            return 0
        else:
            poprawne+=1
    if poprawne == len(imie):
        return 1

lista = []  
for i in open("imiona.txt","r+"):
    lista.append(i.strip())
iterator = 0
koniec = 0
while (koniec!=1):
    imie = input("Podaj imie: ")
    imie = imie.capitalize()
    if (imie == "Koniec"):
        koniec = 1
    if (sprawdz(imie) == 1 and imie!="Koniec"):
        if imie in lista:
            print("Podano już to imie")
        else:
            lista.append(imie)
            iterator +=1
lista.sort()
plik = open("imionaoutput.txt","w+")
for i in lista:
    plik.write("%s\n" % i)
plik.close()
"""


"""5
import pickle
def sprawdz(imie):
    poprawne = 0
    for litera in imie:
        if (litera.isalpha() == False):
            print("Imiona nie zawierają cyfr")
            return 0
        else:
            poprawne+=1
    if poprawne == len(imie):
        return 1

imiona_meskie = ["Kosma", "Barnaba", "Bonawentura", "Jarema","Kuba"]
lista_m =["Imiona męskie: \n"]
lista_k =["Imiona żeńskie: \n"]
iterator = 0
koniec = 0
while (koniec!=1):
    imie = input("Podaj imie: ")
    imie = imie.capitalize()
    if (imie == "Koniec"):
        koniec = 1
    if (sprawdz(imie) == 1 and imie!="Koniec"):
        if (imie[len(imie)-1]!='a' or (imie in imiona_meskie)):
            if imie in lista_m:
                print("Podano już to imie")
            else:
                lista_m.append(imie+'\n')
                iterator +=1
        else:
            if imie in lista_k:
                print("Podano już to imie")
            else:
                lista_k.append(imie+'\n')
                iterator +=1            
pickle.dump(lista_m,open("imionambinary.p","wb"))
pickle.dump(lista_k,open("imionakbinary.p","wb"))

"""

"""6
import os
import pickle

def sprawdz(imie):
    poprawne = 0
    for litera in imie:
        if (litera.isalpha() == False):
            print("Imiona nie zawierają cyfr")
            return 0
        else:
            poprawne+=1
    if poprawne == len(imie):
        return 1

lista_k=[]
lista_m=[]
if os.path.getsize("imionakbinary.p") > 0:      
    with open("imionakbinary.p", "rb") as f:
        unpickler = pickle.Unpickler(f)
        lista_k = unpickler.load()
if os.path.getsize("imionambinary.p") > 0:      
    with open("imionambinary.p", "rb") as f:
        unpickler = pickle.Unpickler(f)
        lista_m = unpickler.load()
imiona_meskie = ["Kosma", "Barnaba", "Bonawentura", "Jarema","Kuba"]
iterator = 0
koniec = 0
while (koniec!=1):
    imie = input("Podaj imie: ")
    imie = imie.capitalize()
    if (imie == "Koniec"):
        koniec = 1
    if (sprawdz(imie) == 1 and imie!="Koniec"):
        if (imie[len(imie)-1]!='a' or (imie in imiona_meskie)):
            if imie in lista_m:
                print("Podano już to imie")
            else:
                lista_m.append(imie+'\n')
                iterator +=1
        else:
            if imie in lista_k:
                print("Podano już to imie")
            else:
                lista_k.append(imie+'\n')
                iterator +=1            
pickle.dump(lista_m,open("imionambinary.p","wb"))
pickle.dump(lista_k,open("imionakbinary.p","wb"))
"""

"""SPRAWDZANIE PICKLA
import os
import pickle
imiona_k=[]
imiona_m=[]
if os.path.getsize("imionakbinary.p") > 0:      
    with open("imionakbinary.p", "rb") as f:
        unpickler = pickle.Unpickler(f)
        imiona_k = unpickler.load()
if os.path.getsize("imionambinary.p") > 0:      
    with open("imionambinary.p", "rb") as f:
        unpickler = pickle.Unpickler(f)
        imiona_m = unpickler.load()
print(imiona_m)
print(imiona_k)
"""
