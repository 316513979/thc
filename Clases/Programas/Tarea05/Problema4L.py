def fib(n):
    i=2
    a=0
    b=1
    F=[0, 1]
    if n<3:
        if n==1:
            F.pop(1)
            return F
        else:
            return F
    else:
        while i<n:
            i=i+1
            a,b = b,a+b
            F.append(b)
        return F
