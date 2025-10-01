# Forma Condicional 1

"""
senha = 123 # Estamos inicializando a variável

while senha != 1234:
    senha = int (input('informe sua senha: '))

print ('Obrigado por usar esse sistema')

"""


# Forma Condicional 2


Tentativas = 3
while True: 
    senha = input("Informe sua semha: ")

    if senha == "aluno2" and Tentativas > 0:
        print('Parabéns senha correta')
        break # este comando ira encerrar o while. 


    if Tentativas > 0:
        Tentativas -= 1 # esta diminuindo as tentativas
        
        if Tentativas <= 0:
            print("Sem tentativas so lamento")
            break