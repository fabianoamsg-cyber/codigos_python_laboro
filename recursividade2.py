# Função que irá somar valores
def soma_ate(n):
    print(f'Entrando na soma_ate({n})')
    if n == 1:
       print(f'-> Caso Base! Retornando 1')
       return 1  # Caso base: se n for 1, retorna 1

       # Caso recursivo: n + soma dos anteriores
    resultado = n + soma_ate(n - 1)
    print(f'<- Retornando {n} + .... = {resultado}')

    return resultado

# Chamando a função e imprimindo o resultado
print(soma_ate(3))  # Saída: 6 (3 + 2 + 1)

