def maximo(n, k, y):
    if n>k and n>y:
        return n
    if k>n and k>y:
        return k
    if y>n and y>k:
        return y
    if n==k==y:
        return n