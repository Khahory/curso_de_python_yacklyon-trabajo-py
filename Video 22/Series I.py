#generar multiplo de 3

num = int(input("Digita la cantidad de veces que se mostrara el multiplo: "))
interructor = 3

for i in range(1, num+1):
    print(interructor, end=", ")
    interructor = interructor + 3