# Calcular el promedio de 3 calificaciones

import os

os.system('clear')
print('Calculamndo el promedio de 3 calicaciones de tipo entero')

print('Dame 3 calificaciones separadas por espacio: ')
c1, c2, c3 = input().split() # split divide la cadena en partes en base al espacio
c1, c2, c3 = int(c1), int(c2), int(c3)

prom = ( c1 + c2 + c3) / 3

print(f'El promedio de: {c1}, {c2}, {c3} es {prom:.0f}')



