def main():
    napis = '''To    jest        jakiś
rozstrzelony tekst!'''

    napis = napis.replace('\n', " ")
    napis = napis.split()
    napis = " ".join(napis)
    print(napis)


if __name__ == '__main__':
    main()