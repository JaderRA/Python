#Recebe a largura e altura de um retângulo e devolve o retângulo
l=int(input("Informe a largura do retângulo: "))
h=int(input("Informe a altura do retângulo: "))
n=0
i=0
while n<h:
    while i<l:
        print("#", end='')
        i+=1
    n+=1
    i=0
    print()

    