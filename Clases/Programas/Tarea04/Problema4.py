
def fib(n):
    i=2
    a=0
    b=1
    if n<3:
        if n == 1:
            return 0
        else:
            return 1
    else:
        while i<n:
            i=i+1
            a,b = b,a+b
        return b
        
