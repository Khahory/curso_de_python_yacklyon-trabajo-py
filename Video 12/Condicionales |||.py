valor = int(input("Ingrese un numero: \n"))
if valor < 0:
    res = "El valor es negativo"

elif valor > 0:
    res = "El valor es positivo"

else: res = "El valor es neutro"

print (res)