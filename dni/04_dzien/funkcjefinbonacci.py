def fibonacci(m):
    lista = [0,1]
    
    for i in range(2, m+1):
        # lista[i] = lista[i-1] + lista[i-2]
        lista.append(lista[i-1] + lista[i-2])
    return lista[-1]

wartosc = fibonacci(10)
print(wartosc)

