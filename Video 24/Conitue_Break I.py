print("Identificar pares e impares")
n1 = int(input("Digita el valor inicial: "))
n2 = int(input("Digita un valor mayor o igual al anterior: "))

if n2 < n1:
    print("Error if")
else:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            continue #Salta a la siguente instruccion que es donde esta el else
            print(f"El numero {i} es par")
        else:
            break #Rompe el ciclo o salir del bucle
            print(f"El numero {i} es impar")
