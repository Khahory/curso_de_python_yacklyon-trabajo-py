#serie a,b,a,b,a,b....

limite = int(input("Digite las veces que se repetira: "))
interructor = 2
controlador = 0
letra = ""

while controlador < limite:
    controlador = controlador + 1
    if interructor > 1:
        letra = "A"
        interructor = interructor - 1
    else:
        letra = "B"
        interructor = 2
    print(letra, end=", ")
