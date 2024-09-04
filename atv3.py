#3. Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.

# Solicitar ao usuário que insira um número inteiro
try:
    numero = int(input("Digite um número inteiro: "))

    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except Exception :
    print("Entrada inválida. Por favor, digite um número inteiro.}")
