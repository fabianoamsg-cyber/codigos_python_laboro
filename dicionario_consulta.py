Alimentos = {"arroz": 5.99, "feijao": 7.49, "macarrao": 4.29, "carne": 19.99, "frango": 12.49}

"""
Dicionário é composto de pares chave-valor. As chaves são únicas e servem para acessar os valores associados a elas.
Neste exemplo, temos um dicionário chamado 'Alimentos' onde as chaves são os nomes dos alimentos e os valores são os preços correspondentes.
O dicionário é definido usando chaves {} e os pares chave-valor são separados por vírgulas.

Dicionario
chave: valor -> item

chave: key
valor: value
item: item

"""

print(Alimentos)

# Acessando apenas as chaves do dicionário

for chave in Alimentos.keys():
    print(chave)

# Acessando apenas as valores do dicionário

for valor in Alimentos.values():
    print(valor)

# Acessando os itens (pares chave-valor) do dicionário
for chave, valor in Alimentos.items():
    print(f'Chave: {chave}, Valor: {valor}')

