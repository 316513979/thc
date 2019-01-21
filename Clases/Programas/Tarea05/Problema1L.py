def mcd(a, b):
    if b<a:
        r = a%b
        L=[(a%b)]
        while r>0:
            a=b
            b=r
            r=a%b
            L.append(r)
    else:
        r = b%a
        L=[(b%a)]
        while r>0:
            b=a
            a=r
            r=b%a
            L.append(r)
    return L
            
