min = int(input("Podaj dolny zakres: "))
max = int(input("Podaj górny zakres: "))

for i in range(min, max+1):
    if (i % 2) == 1 and (i % 17) == 0:
        print(i)
