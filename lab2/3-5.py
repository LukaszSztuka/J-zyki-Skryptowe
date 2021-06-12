x = int(input("Podaj rok: "))

if ((x % 4) == 0 and (x % 100) != 0) or ((x % 400) == 0):
    print("Podany rok jest rokiem przestepnym!")
else:
    print("Podany rok nie jest rokiem przestepnym!")
