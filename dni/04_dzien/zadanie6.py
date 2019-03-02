# lista.append()
# range(2, m+1)
# for

lista = [0,1]
m = 17
for i in range(2, m+1):
    # lista[i] = lista[i-1] + lista[i-2]
    lista.append(lista[i-1] + lista[i-2])
    print(lista)