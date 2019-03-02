uczestnik = 'Piotr'

dziennik = ['Piotr','Adam','Jozek','Tomek','Konrad', 'Piotr']

# if 'Piotr' 
#  print('Piotr')
#  else ('To nie jest Piotr')




#  for zmienna in dziennik 
    # pass


# for piotr in lista_imion:
    
    # czym sie rozni pass od print?
    #   if piotr == piotr
    # print('Piotr')
    # else('To nie jest Piotr')

    
for uczen in dziennik:
    if uczen == uczestnik:
        print("znalazlem cie:", uczen)
    else:
        print('nie znalazlem')


for pozycja, uczen in enumerate(dziennik):
#     print(pozycja, “: “, uczen)
    if uczen == uczestnik:
        print('Piotr', pozycja)
    # pokazuje Piotr pozycja 0 Piotr pozycja 5

