#saber si es par o impar

#Nota (El residuo se busca con %, 4%2 = 0, es el resultado final que esta abajo de)

A = int(input("Digita el valor a \n"))

if A % 2 == 0:
    print ("El valor {} es par" .format(A) )
else:
    print ("El valor {} es impar")