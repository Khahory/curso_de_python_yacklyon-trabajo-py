#En OneNote estan los metodos para el uso de los diccionarios (basico)

edades = {"Angel":20, "Jason":18, "Aura":12, "Maria":40}
print(edades)

print("\033[;36m"+"-------------------------------------"+'\033[0;m')

edades = {"Angel":20, "Jason":18, "Aura":12, "Maria":40}
diccionario = edades.copy() #Copy and paste
print(diccionario)

print("\033[;36m"+"-------------------------------------"+'\033[0;m')

notas = dict.fromkeys(["Angel","Jason","Aura", "Maria"], 100)
print(notas)

print("\033[;36m"+"-------------------------------------"+'\033[0;m')

edades = {"Angel":20, "Jason":18, "Aura":12, "Maria":40}
print(edades.get("Angel"))

print("\033[;36m"+"-------------------------------------"+'\033[0;m')

edades = {"Angel":20, "Jason":18, "Aura":12, "Maria":40}
print(edades.items()) #Agrupados en pares

print("\033[;36m"+"-------------------------------------"+'\033[0;m')