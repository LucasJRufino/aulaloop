numeroSecreto = 42
tentativa = 1
while tentativa <= 3:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite == numeroSecreto:
        print("Parabéns você acertou!")
        break
    else:
        if palpite > numeroSecreto:
            print("O número secreto é menor que ", palpite)
        else:
            print ("O número secreto é maior que ", palpite)
    tentativa += 1

if tentativa > 3:
    print("Suas tentativas acabaram. O número secreto era: ", numeroSecreto)