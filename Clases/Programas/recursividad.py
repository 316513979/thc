# -*- coding: utf-8 -*-
def fib(n):
    """ Calcula el nesimo término
de la sucesión de fibonacci con n natural
"""
    if n>2:
        return fib(n-1)+fib(n-2)
    else:
        return 1

print fib(1)
print fib(2)
print fib(5)
print fib(10)

def gauss(n):
    if 1<n:
        return gauss(n-1)+n
    else:
        return 1

# Mi versión:

def printr (L):
    A=L
    if 1<len(A):
        print A[0],
        A.pop(0)
        printr (A)
    else:
        print A[0],

# Las versiones del profesor:

def printr1(L):
    if L:
        print L[0],
        printr(L[1:])
    else:
        None
        
def printr2(L):
    if len(L)>1:
        print L[0],
        printr(L[1:])
    else:
        None
                

