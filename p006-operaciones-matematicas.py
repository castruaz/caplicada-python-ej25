# Ejemplifica las operaciones matematicas basicas

import os;os.system('clear')

# dato de prueba
#x = 10.5
#y = 2.5

x = float(input('Valor de x  ? '))
y = float(input('Valor de y  ? '))

suma  = x + y
resta = x - y
mult  = x * y
div   = x / y
res   = x % y
pot   = x ** y
dive  = x // y

print(f'Suma : {suma}\nResta: {resta}\nMultiplicacion: {mult}\nDivisio: {div}')
print(f'Residuo: {res}\nPotencia: {pot}\nDivision Entera: {dive}')