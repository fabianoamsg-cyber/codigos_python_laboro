# Contagem com recursividade
def Contagem(num):

    if num>=1:
        print(num)
        num = num - 1
        Contagem(num)  #chamada recursiva

#chamando a função
Contagem(10)