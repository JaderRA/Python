n=int(input("Digite o valor de n: "))
fatorial=1
while n>=0:
    if n==0 or n==1:
        fatorial=fatorial*1
    else:
        fatorial=fatorial*n
    n=n-1
print("", fatorial)