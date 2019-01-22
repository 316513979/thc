def divisibilidad(a):
    i=1
    L=[]
    while 1<=i and i<=a:
        r=a%i
        if r == 0:
            L.append (i)
        i=i+1
    return L
