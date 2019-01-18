# -*- coding: utf-8 -*-
# En este ejercicio se pretendía calcular el máximo común divisor de dos enteros cualesquiera. 
def mcd(a, b):
    r = a%b
    if r>0:
        while r>0:
            if r%b>0:
                b ,r= r, r%b
                return r
            else:
                return r
    else:
        return b
            

def mcd1(x, y):
    i=1
    while i<x and i<y:
        if (x/i)*i == (y/i)*i:
            print i
        else:
            i=i+1
            
def divisores(x):
    i=0
    while i<x:
        i=i+1
        if (x/i)*i == x:
        return

a=10
b=3
s=a-b
while s>0:
	if s-b>0:
		s=s-b
		print s
	else:
		print s




    
            
