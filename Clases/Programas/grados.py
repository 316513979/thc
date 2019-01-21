# -*- coding: utf-8 -*-

def listaC(Cmin, Cmax, n):
    gradosC = []
    dC= (Cmax - Cmin)/float(n-1)
    # equivalente a for(i=0;i<n;i++) en otros programas
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)
    return gradosC

def listaF(gradosC):
    gradosF = []
    for C in gradosC:
        F = (9.0/5)* C +32
        gradosF.append(F)
    return gradosF

def mostrarListas(gradosC, gradosF):
    for i in range(len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]
        print ("%5.1f %5.1f" % (C, F))






# Las primeras dos funciones tienen una naturaleza distinta a la tercera: las
# primeras regresan un objeto (valor) mientras que la última imprime resultados.
