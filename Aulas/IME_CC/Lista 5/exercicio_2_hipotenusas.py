def soma_hipotenusas(n):
    hip=[]
    cont=0
    pos=0
    for i in range (1,n+1):
        for j in range (1, n+1):
            for l in range (1, n+1):
                if (i**2)==((j**2)+(l**2)):
                    print(i, j, l)
                    cont+=1
        if cont!=0:
            hip.insert(pos, i)
            pos+=1
            cont=0
    soma=sum(hip)
    return soma


