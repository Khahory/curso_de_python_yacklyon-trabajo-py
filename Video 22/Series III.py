#serie a,b,a,b,a,b....

limite = int(input("Digite las veces que se repetira: "))
interructor = True
controlador = 0
letra = ""

while controlador < limite:
    controlador = controlador + 1
    if interructor:
        letra = "A"
        interructor = False
    else:
        letra = "B"
        interructor = True
    print(letra, end=", ")
