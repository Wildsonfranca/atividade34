#1. Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.



# Solicitar ao usuário que insira um número
try:
    entrada = input('Digite um número: ')

# Converter a entrada para o tipo float
    numero = float(entrada)

# Exibir o número e seu tipo de dado
    print(f'Número digitado: {numero}')
    print(f'Tipo de dado: {type(numero)}')

except Exception as e:
    print(f'Não foi possível realizar a operação.{e}')


