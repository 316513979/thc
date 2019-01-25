# -*- coding: utf-8 -*-
import Problema7AP

def prueba_H_eps():
    e=0.01
    float(e)
    V=[-2*e, -e, 0, e, 2*e]      # Escogí estos valores de e porque las expresiones se ven más ordenadas. 
    for valor in V:
        if valor<-e:
            print 'El valor de la función para x<-%.2f es: ' % (e)
            print Problema7AP.H_eps(valor)
        elif valor==-e:
            print 'El valor de la función para x=%.2f es: ' % (valor)
            print Problema7AP.H_eps(valor)
        elif valor == 0:
            print 'El valor de la función para x=%.2f es: ' % (valor)
            print Problema7AP.H_eps(valor)    
        elif valor==e:
            print 'El valor de la función para x=%.2f es: ' % (valor)
            print Problema7AP.H_eps(valor)
        else:
            print 'El valor de la función para %.2f<x es: ' % (e)
            print Problema7AP.H_eps(valor)
        

