def fatorial (n):
    x=1
    while n>=0:
        if n==0 or n==1:
            x=x*1
        else:
            x=x*n
        n=n-1
    return x

def binomio(y, k):
    if y<k:
        b=0
    else:
        b=fatorial(y)/(fatorial(k)*fatorial(y-k))
    return b





