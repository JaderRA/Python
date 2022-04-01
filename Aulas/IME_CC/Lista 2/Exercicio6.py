#Distância entre dois pontos
x1=int(input("Digite a coordenada x do primeiro ponto: "))
y1=int(input("Digite a coordenada y do segundo ponto: "))
x2=int(input("Digite a coordenada x do segundo ponto: "))
y2=int(input("Digite a coordenada y do segundo ponto: "))
dist=(((x1-x2)**2)+((y1-y2)**2))**0.5
if dist>=10:
    print("longe")
else:
    print("perto")