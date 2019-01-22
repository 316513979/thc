def divisibilidad(a):
    i=1
    print '%d es divisible entre: ' % (a)
    while 1<=i and i<=a:
        r=a%i
        if r == 0:
            print i
        i=i+1
        
