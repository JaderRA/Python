#Converte a temperatura de Celsius para Farenheit e vice-versa

ativador=input("Entre a escala em que está a temperatura: C para Celsius e F para Farenheit: ")

valorabs=input("Entre o valor numérico da temperatura (apenas o número): ")
valorabs=float(valorabs)

if ativador == "c" or "C":
    tempF = ((valorabs*9)/5)+32
    print("\n")
    print("A temperatura em Farenheit é: ", int(tempF), "º F")

else:
    tempC = ((valorabs-32)*5)/9
    print("\n")
    print("A temperatura em Celsius é: ", int(tempC), "º C")