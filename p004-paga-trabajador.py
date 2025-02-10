# Calcular la paga total de un trabajador en base a las horas trabajadas y a la paga por hora
# entrada : nombre (str), horas (int), paga (float)
# salida  : pagabruta (antes de impuesto), impuesto (paga * tasa), paganeta (pata despues de impuesto)

print('Calculando la paga de un trabajador \n')

# Entrada de datos
nombre = input('Nombre del trabajador : ')
horas  = int(input('Horas trabajadas      : '))
paga   = float(input('Paga x hora trabajada : '))
tasa   = 0.03

# Calculos
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
# Salida
print('\nResumen de pagos')
print(f'El trabajador {nombre}, trabajo {horas} horas, a un paga de {paga} pesos, a una tasa de {tasa} de impuesto')
print(f'Paga Bruta (antes de impuesto) : {pagabruta:,.2f}')
print(f'Impuesto                       : {impuesto:,.2f}')
print(f'Paga Neta (despues de impuesto): {paganeta:,.2f}')


