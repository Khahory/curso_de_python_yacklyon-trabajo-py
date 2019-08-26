#serie 4,3,2,1, 4,3,2,1

limite = int(input("Ingrese un la veces que se reperira: "))
interructor = 4
controlador = 0

while controlador < limite:
    print(interructor)
    controlador = controlador + 1
    if interructor > 1:
        interructor = interructor - 1
    else:
        interructor = 4


