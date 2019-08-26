#Calcular numeros random que no pasen de 10

import random

def vectro_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(0,10)
    return vector

print("Ingrese el limite de veces a mostrar numeros")
print(vectro_aleatorio(int(input())))