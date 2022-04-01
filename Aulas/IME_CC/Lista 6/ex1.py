#Lê uma sequência de números e imprime na ordem inversa

vetor=[]
n=1

while n!=0:
    n=int(input("Entre o número: "))
    vetor.append(n)

print(vetor[::-1])


