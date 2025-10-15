# Tupla: Conjunto de dados
# Uma tupla é uma estrutura de dados que armazena uma coleção ordenada e imutável de elementos.
# As tuplas são semelhantes às listas, mas diferem em alguns aspectos importantes.

# Criando uma Tupla
frutas = ("banana", "uva","morango", "acerola")

#print(type(frutas))

print(frutas)

frutas[2] = 'manga' #aqui teremos um erro

print(frutas[2])

# Exibir todas as frutas

for item in frutas:
    print(item)