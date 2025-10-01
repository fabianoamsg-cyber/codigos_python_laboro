while True:
    num = int(input("Digite um número inteiro (0 para sair): "))
    
    if num == 0:
        break
    
    if num % 2 != 0:
        print(f"Número ímpar: {num}")
