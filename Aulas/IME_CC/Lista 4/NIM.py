def computador_escolhe_jogada(n, m):
    pecas_retiradas=0
    for i in range((n-1), 0, -1):
        if i%(m+1)==0 and (m+1)!=n:
            cheat=i
            pecas_retiradas=n-cheat
            return pecas_retiradas
    if n<m:
        pecas_retiradas=n
        return pecas_retiradas
    else:
        pecas_retiradas=m
        return pecas_retiradas
       
def usuario_escolhe_jogada(n, m):
    pecas_jogador=int(input("Quantas peças você vai tirar? "))
    while pecas_jogador>m or pecas_jogador<=0:
        print("Jogada inválida! Tente de novo.")
        pecas_jogador=int(input("\n\nQuantas peças você vai tirar? "))
    return pecas_jogador

def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    while m>n:
        m=int(input("Ops, valor inválido! Digite novamente: "))
    if n%(m+1)==0:
        print("Você começa\n")
        while n>m and n>=0:
            o=usuario_escolhe_jogada(n,m)
            print("Você tirou", o, "peças.")
            print("Agora restam", (n-o), "peças no tabuleiro")
            n=n-o
            o=computador_escolhe_jogada(n,m)
            print("\nComputador tirou", o, "peças.")
            print("Agora restam", (n-o), "peças no tabuleiro\n")
            n=n-o
            if n<=m and n!=0:
                o=computador_escolhe_jogada(n,m)
                print("Computador tirou", o, "peças.\n")
                print("Agora restam", (n-o), "peças no tabuleiro")
                print("Fim de jogo! O computador ganhou\n")
            elif n==0:
                print("Fim de jogo! O computador ganhou\n")
    else:
        print("Computador Começa\n")
        while n>m and n>=0:
            o=computador_escolhe_jogada(n,m)
            print("\nComputador tirou", o, "peças.")
            print("Agora restam", (n-o), "peças no tabuleiro\n")
            n=n-o
            o=usuario_escolhe_jogada(n,m)
            print("Você tirou", o, "peças.")
            print("Agora restam", (n-o), "peças no tabuleiro\n")
            n=n-o
            if n<=m:
                o=computador_escolhe_jogada(n,m)
                print("Computador tirou", o, "peças.\n")
                print("Agora restam", (n-o), "peças no tabuleiro")
                print("Fim de jogo! O computador ganhou\n")
            elif n==0:
                print("Fim de jogo! O computador ganhou\n")

def campeonato():
    print("Você escolheu campeonato!")
    rodada=1
    placar_computador=0
    while rodada!=4:
        print("*** Rodada", rodada, "***")
        partida()
        placar_computador+=1
        rodada+=1
    print("***Final do Campeonato!***\n")
    print("Placar: Você: 0 X", placar_computador, "Computador")
 
print("Bem vindo ao jogo do NIM! Escolha: ")
tipo_jogo=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
if tipo_jogo==1:
    partida()
elif tipo_jogo==2:
    campeonato()
else:
    while tipo_jogo!=1 or tipo_jogo!=2:
        print("Opção inválida! Tente novamente:")
        tipo_jogo=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
