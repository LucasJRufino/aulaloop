tentativas = 0
while tentativas < 3:
    senha = input("senha")
    if senha == "Senha123":
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas += 1
    
else:
    print("Você excedeu o número máximo de tentativas")