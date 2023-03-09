palavrasSemVogais = ""

usuarioPalavra = input("Entre com uma palavra: ")
usuarioPalavra = usuarioPalavra.upper()

for letra in usuarioPalavra:
    if letra == "A":
        continue
    if letra == "E":
        continue
    if letra == "I":
        continue
    if letra == "O":
        continue
    if letra == "U":
        continue
    else:
        palavrasSemVogais += letra
    
print(palavrasSemVogais)