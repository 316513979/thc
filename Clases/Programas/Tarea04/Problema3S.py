#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es crear un convertidor de escalas de temperatura:
# centígrados a fahrenheit y viceversa. 

import Problema3
print 'El texto se escribe entre comillas'
a=input ('Convertir de grados (centígrados o fahrenheit)')
b=input ('a grados (centígrados o fahrenheit)')

if a == 'centígrados' and b == 'fahrenheit':
    x= input ('Introduce la temperatura en grados centígrados: ')
    print Problema3.CentigradosFahrenheit (x)
else:
    if a == 'fahrenheit' and b == 'centígrados':
        x= input ('Introduce la temperatura en grados fahrenheit: ')
        print Problema3.FahrenheitCentigrados (x)
    else:
        print ('Error')
        
    
