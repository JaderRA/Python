#Recebe um número n maior que dois e checa quantos primos existem no intervalo de 2 a n
def n_primos(n):
    cont=0
    primo=0
    for i in range(2, n+1):
        for p in range(2, n+1):
            x=i%p
            if x==0:
                cont+=1
        if cont==1:
            primo+=1
        cont=0
    return primo
