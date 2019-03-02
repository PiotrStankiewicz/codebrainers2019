# wypisz liczby od 1-100
# /3 fizz
# /5 Buzz
# 15 FizzBuzz

for wypisz in range(1,101):
    print (wypisz)
    if wypisz % 15 == 0:
        print('FizzBuzz', wypisz)
    elif wypisz % 3 == 0:
        print('Fizz', wypisz) 
    elif wypisz % 5 == 0:
        print('Buzz', wypisz)
    
    


liczby = [1,10,25,26,50,100]

for pierwsza in liczby:
    print(pierwsza)