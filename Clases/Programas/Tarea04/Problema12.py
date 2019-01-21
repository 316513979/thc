def mcm(a, b):
    while a<b or b<a:
        a=a+a
        b=b+b
    return b
