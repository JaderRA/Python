#Decompor em fatores primos e dar a multiplicidade dos fatores
num=int(input("Digite o número: "))
i=2
if num==0 or num==1:
    print("Número inválido")
    while num==0 or num==1:
        num=int(input("Digite o número: "))    
expoente=0
def primo(i): #checa se um i é primo
    n=0
    cont=0
    while n<=i or cont<2:
        n+=1
        x=i%n
        if x==0:
            cont+=1
    if cont==2:
        return i
while num!=1: #divide num por i 
    while num%i==0:
        primo(i)
        num=num//i
        expoente+=1
    if expoente!=0:
        print("", i, "^", expoente)
    i+=1
    expoente=0



