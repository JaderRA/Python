def maior_primo(p):
    for n in range(2, p+1):
        if n>1:
            for i in range(2, n):
                if (n%i)==0:
                    break
            else:
                primo=n
    return primo

