#Lê uma sequência de números e imprime na ordem inversa

vetor=[]
n=1

while n!=0:
    n=int(input("Entre o número: "))
    vetor.append(n)

vetor.remove(0)
x=vetor[::-1]
for i in x:
    print(i)