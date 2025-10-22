agenda = dict() # INICIALIZANDO DICIONARIO COM A FUNCAO DICT

while True:
    print('\nAgenda Eletronica\n')
    print('1 - Adicionar contato')
    print('2 - Excluir contato')   
    print('3 - Sair do sistema')
    resposta = input('Escolha uma opcao: ')

    if resposta == '1':
        nome = input('Informe o nome do contato: ')
        agenda[nome] = input(f'Informe o telefone do contato de {nome}: ')

        print('\nContato adicionado com sucesso!\n')
        print(agenda)

    elif resposta == '2':
        print(agenda)
        escolha = input('Informe o nome do contato que deseja excluir: ')

# VERIFICANDO SE O CONTATO EXISTE ANTES DE EXCLUIR
        if escolha in agenda:

            del agenda[escolha]
            print('\nContato excluido com sucesso!\n')
            print(agenda)

        else:
            print('\nContato nao encontrado!\n')
            print('\nContato excluido com sucesso!\n')
            print(agenda)

    elif resposta == '3':
        print('\nPrograma Encerrado\n')
        break
