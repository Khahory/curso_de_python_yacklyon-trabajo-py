contador = int(input("Digita el conador: "))
if contador < 1:
    print("Error")

else:
    numero = int(input("Digita el primer numero: "))
    for i in range(contador - 1):
        siguiente = int(input(f" Escribe un numero mas alto que {numero} \n"))
        if siguiente < numero:
            print("El numero no es mas alto que el anterior")
            break
        else:
            numero = siguiente
    print("Gracias por participar")