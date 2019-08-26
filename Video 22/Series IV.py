#Serie fibonacci
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21

# A + B = C
# b + c = D

#Valores
A = 1
B = 1
C = 0
limite = int(input("Digite el limite de veces: "))
interructor = 0

if limite < 1:
    print("Error")
elif limite == 1:
    print(A)
else:
    while interructor < limite:
        print(A, end=", ")
        C = A + B
        #Actualizar datos
        interructor += 1
        A = B
        B = C