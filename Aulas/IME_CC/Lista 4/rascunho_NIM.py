def computador_escolhe_jogada(n, m):
    pecas_retiradas=0
    for i in range((n-1), 0, -1):
        if i%(m+1)==0 and (m+1)!=n:
            cheat=i
            pecas_retiradas=n-cheat
            return pecas_retiradas
        elif n<m:
            pecas_retiradas=n
    else:
        pecas_retiradas=m
        return pecas_retiradas

print(computador_escolhe_jogada(13,11))