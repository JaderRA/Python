#Recebe o grau esférico esquerdo e direito e o grau cilíndrico esquerdo e direito, compara e sugere a lente adequada

print("Bem vindo à nossa loja!")

gesferico_esquerdo=1
while gesferico_esquerdo>0 or gesferico_esquerdo<-15:
    gesferico_esquerdo=float(input("Insira o grau esférico do olho esquerdo: "))
    if gesferico_esquerdo>0 or gesferico_esquerdo<-15:
        print("Valor incorreto. Por favor insira um valor entre 0 e -15:")

gesferico_direito=1
while gesferico_direito>0 or gesferico_direito<-15:
    gesferico_direito=float(input("Insira o grau esférico do olho direito: "))
    if gesferico_direito>0 or gesferico_direito<-15:
        print("Valor incorreto. Por favor insira um valor entre 0 e -15:")

gcilindrico_esquerdo=1
while gcilindrico_esquerdo>0 or gcilindrico_esquerdo<-6:
    gcilindrico_esquerdo=float(input("Insira o grau cilíndrico do olho esquerdo: "))
    if gcilindrico_esquerdo>0 or gcilindrico_esquerdo<-6:
        print("Valor incorreto. Por favor insira um valor entre 0 e -6:")

gcilindrico_direito=1
while gcilindrico_direito>0 or gcilindrico_direito<-6:
    gcilindrico_direito=float(input("Insira o grau cilíndrico do olho direito: "))
    if gcilindrico_direito>0 or gcilindrico_direito<-6:
        print("Valor incorreto. Por favor insira um valor entre 0 e -6:")


if gcilindrico_direito==0 and gcilindrico_esquerdo==0 and -12<=gesferico_direito<=-3 or -12<=gesferico_esquerdo<=-3:
    print("A lente indicada no seu caso é a Prime")

elif -2<=gcilindrico_direito<=0 or -2<=gcilindrico_direito<=0 and -10<=gesferico_direito<=-3 or -10<=gesferico_esquerdo<=-3:
    print("A lente indicada no seu caso é a Prime")

elif -5<=gcilindrico_direito<-2 and -5<=gcilindrico_esquerdo<-2:
    print("A lente indicada para o seu caso é a Vision")

else:
    print("Desculpe, não possuímos produtos para grau cilíndrico menor que -5.")