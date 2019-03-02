# 1tekst 2slownik dict() 3petla 4print(wystapienia)
tekst = 'ala ma kota a kot ma ale'
slownik = dict()
for literka in tekst:
    # slownik[literka] += 1
    
    if literka in slownik:
        slownik[literka] += 1
    else:
        slownik[literka] = 1
print(slownik)