numero=int(input("Digite um número inteiro: "))
soma=0
while numero!=0:
    algarismo = numero%10
    numero=numero//10
    soma = soma+algarismo
print("", soma)

