# -*- coding: utf-8 -*-


X=[]    # Esta lista corresponde a los puntos del eje X.
i=-5
while -5<=i and i<=5:     # Escogí utilizar un while para hacer las listas porque
    X.append(i)           # ni for ni range permiten incrementos del tipo flotante.
    i += 0.5              # El ciclo while toma cada valor desde el -5 hasta el 5
                          # y lo introduce en la lista de modo que cada uno difiere del otro 0.5.
Y=[]
j=-7
while -7<=j and j<=7:
    Y.append(j)
    j += 0.5

Plano=[]
for x in X:               # Por cada elemento del eje x se forma una lista en la que está ese elemento y un elemnto del eje Y.
    for y in Y:           # Al final cada elemento del eje x tiene una lista con cada elemento del eje y: estos son los puntos del plano.
        punto=[x, y]      # Cada lista se mete dentro de una lista que representa el plano. 
        Plano.append(punto)

