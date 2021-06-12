def main():
    n = '''Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno Święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem 
(Gdy od płaczącej matki pod Twoję opiekę
Ofiarowany, martwą podniosłem powiekę
I zaraz mogłem pieszo do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moję duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane, jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą.'''

    samogloski = ['a', 'e', 'y', 'i', 'o', 'ą', 'ę', 'u', 'ó']

    spolgoski = ['b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'y', 'z', 'ż', 'ź']

    liczba_znakow = len(n)
    liczba_spacji = n.count(' ')
    liczba_samoglosek = 0
    liczba_spolgosek = 0
    for c in n:
        if c.lower() in samogloski:
            liczba_samoglosek += 1
        elif c.lower() in spolgoski:
            liczba_spolgosek += 1

    liczba_innych_znakow = liczba_znakow-liczba_spolgosek-liczba_samoglosek-liczba_spacji
    print("Tekst składa sie z: %s znaków, w tym: %s samogłosek, %s spółgłosek, %s spacji oraz %s innych znaków." % (liczba_znakow, liczba_samoglosek, liczba_spolgosek, liczba_spacji, liczba_innych_znakow))

    print("\nCo drugi znak:")
    print(n[::2])

    print("\nCo trzeci znak:")
    print(n[::3])

    print("\nCo siódmy znak:")
    print(n[::7])

    n = n.split('\n', 1)[0]
    print("\n"+n)
    print("\n"+n.upper())
    print("\n"+n.replace("Litwo", "Polsko"))




if __name__ == '__main__':
    main()