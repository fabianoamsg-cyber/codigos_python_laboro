agenda = {"Maria":1234, "Pedro":4321, "Joana":9876}
contato = {"nome":"Maria", "idade":30}

print(type(agenda))

print(agenda)

print("-"*80)
print(agenda["Maria"]) # Acessando o valor associado a chave "Maria"
print(contato["nome"]) # Acessando o valor associado a chave "nome"

# INSERINDO DADOS NA AGENDA
# Forma 1

agenda["Ana"] = 5678
print(agenda)

# Forma 2
agenda.update({"Joana":8765}) #UPDATE PODE INSERIR OU ATUALIZAR
print(agenda)

# excluindo dados da agenda
# forma 1
agenda.pop("Pedro")
print(agenda)

# forma 2
del agenda["Joana"]
print(agenda)