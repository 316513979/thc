# -*- coding: utf-8 -*-
def convertir(f):
    caprox = (f-32)/2.0
    c= (f-32)*(5.0/9.0)
    d= c-caprox
    print 'grados Fahreheit   grados Celsius fórmula   grados Celsius aprox.   Diferencia' 
    print '%10.3f' %(f),
    print '%20.3f' %(c),
    print '%25.3f'% (caprox),
    print '%17.3f' %(d)
