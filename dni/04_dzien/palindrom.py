# sprawdz czy zadany tekst jest palindromem

tekst = 'kajak'
len(tekst)
# if tekst = 'palindrom'
#     print('to jest palindrom')
# else 
#     print('to nie jest palindrom')

# 

for pozycja, sprawdzenie in enumerate(tekst):
    if tekst[pozycja] == tekst[-pozycja-1]:
        print('jest palindromem')
    else:
        print('nie jest')
        break



fruits = ['jablko','banan', 'gruszka',]

# for owoce in fruits:
#     print(fruits[2])

for nr, warzywa in enumerate(fruits):
    if nr == 1:
        break


    print('start')
    print(nr)
    print(warzywa)
    print('koniec')