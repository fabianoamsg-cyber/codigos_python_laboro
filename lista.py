# Criando uma Lista
numeros = [3,5,8,10,14]

#print(type(lista))

print(numeros)

numeros[2] = 15 # alterando o valor do indice 2


# exibir todos os números
for item in numeros:
    print(item)



# Inserindo valores na lista

numeros.append(23) # adiciona sempre no final
print(numeros)

# adicionando item em qualquer lugar

numeros.insert(2,90) # iremos inserir o valor 90 no indice 2
print(numeros)

#Removendo item da lista
numeros.pop(3)# remeovendo item do final da lista
print(numeros)