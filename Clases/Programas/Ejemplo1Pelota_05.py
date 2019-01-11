# -*- coding: utf-8 -*-
# Diego A. Santillán Arriaga

print 34*3 - 1/2 * 9.81*3**2 # 1/2 calcula la división en enteros (redondea a enteros)
print 34*3 - 1.0/2 * 9.81*3**2 # 1.0/2 calcula la división en punto flotante (muestra decimales)
print 34*1 - 1.0/2 * 9.81*1**2
print 34*1.5 - 1.0/2 * 9.81*1.5**2
print 34*5 - 1.0/2 * 9.81*5**2
v0 = 34  # Cada vez que se asigna una valor a una misma variable este se reescribe
g = 9.81
t = 5
y = v0*t - 1.0/2*g*t**2
print y
print 'La posición de la pelota en el t=%E es %10.2f\n%f' % (t, y, t)

def posicion(t,v0):
    y = v0*t - 1.0/2*g*t**2
    return (y)



print 'Esta \n es \n una cadena \n multilinea '
print '''Esta
es
una cadena
multilínea'''
