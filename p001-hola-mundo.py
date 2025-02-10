# Leer y mostrar datos

print('Leyendo datos del usuario, luego enviar un saludio')
      
nombre = input('Dame tu nombre    : ')
edad   = input('Dame tu edad      : ')
peso   = float( input('Dame tu peso      : ')) # float convierte la cadena introducida a flotante

print(f'{nombre} bienvenido al lenguaje python, tu edad es {edad} y tu peso es {peso} \n')
print('\n\n\n\n')
print(type(nombre))
print(type(edad))
print(type(peso))

 