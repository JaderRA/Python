import random

input_names=input("Digite o nome dos jogadores, separados por um espaço: ")
list_names=input_names.split()

input_loot=input("Entre o loot (need ou greed) para cada jogador, na ordem e separado por espaço: ")
list_loot=input_loot.split()
number_need=[]
i=0
for x in list_loot:
    if x =="need":
        number_need.insert(i, random.randrange(201, 300))
        i = i + 1
    if x =="greed":
        number_need.insert(i, random.randrange(100))
        i=i+1

n=0
for x in number_need:
    if x >= 201:
        print("O jogador", list_names[n], "escolheu need por: ", (x-200))
        n=n+1
    else:
        print("O jogador", list_names[n], "escolheu greed por: ", x)
        n = n + 1

position=number_need.index(max(number_need))

winner = list_names[position]
vroll = number_need[position]

print("\n")

if vroll >=201:
    print ("O jogador", winner, "ganhou o loot com: ", vroll-200 )
else:
    print("O jogador", winner, "ganhou o loot com: ", vroll)


