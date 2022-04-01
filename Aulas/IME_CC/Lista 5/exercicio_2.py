#Recebe a largura e altura de um retângulo e devolve o retângulo, sem preenchimento
l=int(input("Informe a largura do retângulo: "))
h=int(input("Informe a altura do retângulo: "))
n=0
i=0
while n<h:
    while i<l:
        if n==0 or i==0 or n==h-1 or i==l-1:
            print("#", end='')
        else:
            print(" ", end='')
        i+=1
    n+=1
    i=0
    print()
