linha=1
coluna=1
print("***Tabuada***")
while linha<=10:
    while coluna<=10:
        print(linha, "x", coluna, "=", linha*coluna, end="\t")
        coluna+=1
    linha+=1
    print()
    coluna=1