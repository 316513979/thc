# -*- coding: utf-8 -*-
# Un cohete parte del reposo con aceleración constante
# y logra alcanzar en 30 segundos una velocidad de 588 m/s. Calcular
# a) Aceleración
# b) ¿Qué distancia recorrió en esos 30 segundos?

v0 = 0  # velocidad inicial 
vf = 588.0  # velocidad final
t = 30.0  # tiempo
a = (vf-v0)/t   # aceleración a)
d = ((v0+vf)/2)*t  # distancia b)

print a
print d
