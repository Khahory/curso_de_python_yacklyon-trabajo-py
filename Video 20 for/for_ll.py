#Mostrar los numeros forma descendiente
numero = int(input("Digita el numero: \n"))

for i in range(numero, 0, -1):
    print(i)


#La suma de los primeros n numeros
valor = int(input("Digita el numero: \n"))
contador = 0

for i in range(1, valor + 1):
    contador = contador + i
    print(contador)
