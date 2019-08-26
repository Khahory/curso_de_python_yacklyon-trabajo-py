import numpy as np

a = np.array([3,6,2,6,2])
b = np.array([3,1,5,6,21])
print(a+b) # se suman con sus respectivos indices

print("\033[1;33m"+"----------------------------------------"+'\033[0;m')

a = np.array([3,6,2,6,2])
b = np.array([3,1,5,6,21])
print(a>b) # Verifica con sus respectivos indices

print("\033[1;33m"+"----------------------------------------"+'\033[0;m')

a = np.array([3,1,5,6,21])
print(a.argmax()) # Obtiene la posicion del numero mas alto

print("\033[1;33m"+"----------------------------------------"+'\033[0;m')