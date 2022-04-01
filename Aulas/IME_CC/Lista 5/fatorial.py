#Calcula fatorial de vários números, quantas vezes deterinado pelo usuário
n=int(input("Entre a quantidade total de números: "))
i=0
fatorial=1
while i<n:
    num=int(input("Digite o número: "))
    pnum=num
    while num>=0:
        if num==0 or num==1:
            fatorial=fatorial*1
        else:
            fatorial=fatorial*num
        num=num-1
    print("O fatorial de", pnum,"é: ", fatorial)
    i=i+1
