# -*- coding: utf-8 -*-
#Construcción de la malla (Problema4P):

X=[]
i=-5
while -5<=i and i<=5:
    X.append(i)
    i += 0.5

Y=[]
j=-7
while -7<=j and j<=7:
    Y.append(j)
    j += 0.5

Plano=[]
for x in X:
    for y in Y:
        punto=[x, y]
        Plano.append(punto)

#Problema 5P:

Z=[]
for punto in Plano:
    x=punto[0]
    y=punto[1]
    z= ((x**2)/25.0)-((y**2)/49)
    Z.append(z)
    
# El ciclo for toma cada punto del plano, representado por una lista. Luego toma
# los valores dentro de la lista que representan las coordenadas "x" y "y" y calcula el
# valor de z con la fórmula dada. Al final este valor se agrega a la lista Z. 
