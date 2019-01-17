def fib(x):
    i=2
    p=0
    
    if x<3:
        if x == 1:
            print (0)
        else:
            print (1)
    else:
        while i<x:
            i=i+1
            p=p+1
            s=p+(p-1)
        print(s)
