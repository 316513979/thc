# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es crear un convertidor de escalas de temperatura:
# centígrados a fahrenheit y viceversa. 

import Problema3L
print 'Las entradas de texto se deben de escribir entre comillas'
a=input ('Convertir de grados (centígrados o fahrenheit): ')
b=input ('a grados (centígrados o fahrenheit): ')

if a == 'centígrados' and b == 'fahrenheit':
    ti= input ('Introduce la temperatura inicial en grados centígrados: ')
    tf= input ('Ahora introduce la temperatura final en grados centígrados: ' )
    print ('Las equivalencias de grados centígrados a grados fahrenheit son: ')
    print Problema3L.CentigradosFahrenheit (ti, tf)
else:
    if a == 'fahrenheit' and b == 'centígrados':
        ti= input ('Introduce la temperatura inicial en grados fahrenheit: ')
        tf= input ('Ahora introduce la temperatura final en grados fahrenheit: ')
        print ('Las equivalencias de grados fahrenheit a grados centígrados son: ')
        print Problema3L.FahrenheitCentigrados (ti, tf)
    else:
        print ('Error')
