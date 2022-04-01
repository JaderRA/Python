p=10
i=2
cont=0
while i<=p or cont<1:
    x=n%i
    if x==0:
        cont+=1
    if cont==1:
        primo=n
    i+=1
print(primo)

