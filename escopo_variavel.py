valor = 50

def mensagem():
     global valor #declara que a variavel valor é global

     print(f"exibindo a variavel valor {valor}")

     valor = valor + 10
     print(f"valor da variavel atualizada {valor}")

# chamando a função
mensagem()