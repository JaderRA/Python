max=int(input("Digite a quantidade de números a somar:" ))
i=0
soma=0
while i < max:
    valor=int(input("Digite o número a ser somado: "))
    soma=soma+valor
    i +=1
print("O número final é: ", soma)
