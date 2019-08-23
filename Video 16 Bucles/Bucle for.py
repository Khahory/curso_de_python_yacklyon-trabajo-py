#calcular el numero de vocales de una frase

frase = str(input("Digita la frase: "))
vocales = "aeiouAEIOU"
num = 0

for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        num = num + 1
print ("La frase tiene: {} vocales" .format(str(num)))