sito =[True] * 100
sito[0] = False
sito[1] = False

for i in range(2,51):
    n = 2
    wielokrotnosc = n * 1
    while wielokrotnosc < 100:
        sito[wielokrotnosc] = False
        n += 1
        wielokrotnosc = n * 1

for indeks, wartosc in enumerate(sito):
    if wartosc:
        print("Liczba pierwsza:", indeks)