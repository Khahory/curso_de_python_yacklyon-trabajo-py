# Separar uns lista en pares e impares

listaGlobal = [21,43,2,4,5,34,1,3,12,0]

def separar_lista(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares


# print(separar_lista(listaGlobal))

pares, impares = separar_lista(listaGlobal)
print(pares)
print(impares)