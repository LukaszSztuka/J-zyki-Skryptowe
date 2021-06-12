def main():
    pierwsza = input("Podaj pierwsza liczbe: ")
    druga = input("Podaj druga liczbe: ")
    trzecia = input("Podaj trzecia liczbe: ")
    str = pierwsza + druga + trzecia
    liczba = int(str)
    print('Liczba = %s' % liczba)
    liczba = pow(liczba, 2)
    print('kwadrat tej liczby = %s' % liczba)


if __name__ == '__main__':
    main()