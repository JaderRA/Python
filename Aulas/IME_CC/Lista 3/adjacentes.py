num=input("Digite um número inteiro: ")
numero=int(num)
flag=0
for i in num:
    if numero==0:
        break
    alg1=numero%10
    numteste=numero//10
    alg2=numteste%10
    if alg1==alg2:
        print("sim")
        flag=1
        break
    numero=numteste
if flag==0:
    print("não")
