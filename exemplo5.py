maiorNumero = -9999999999
number = int(input("Entre com um número ou digite -1 para parar: "))

while number != -1:
    if number > maiorNumero:
        maiorNumero = number
        
        number = int(input("Entre com um número ou digite -1 para parar: "))
        
print("O maior número é: ", maiorNumero)