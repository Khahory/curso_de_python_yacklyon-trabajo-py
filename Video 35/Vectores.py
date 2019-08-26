#Arreglos

limite = int(input("Digite el limite: "))
multi = int(input("Digite el multiplo: "))

arreglo = []

for i in range(0, limite+1):
    arreglo.append(i*multi)

print(arreglo)