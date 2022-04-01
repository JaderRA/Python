num=int(input("Digite um número inteiro: "))
n=0
cont=0
while n<=num or cont<2:
    n+=1
    x=num%n
    if x==0:
        cont+=1
if cont==2:
    print("primo")
else:
    print("não primo")