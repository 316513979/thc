# -*- coding: utf-8 -*-
from grados import *

L1=listaC(-15, 32, 10)
L2=listaF(L1)
mostrarListas(L1, L2)

a=input ("Cuál es el extremo izquierdo del intervalo")
b=input ("Cuál es el extremo derecho del intervalo")
n=input ("Cuántos subintervalos")
L1 = listaC(a,b,n)
L2 = ListaF(L1)
mostrarListas(L1, L2)

for i, c in enumerate(L1):
    L1[i] = c+5
    print i, c

n=12; gradosC = [-5 + i*0.5 for i in range (n)]

