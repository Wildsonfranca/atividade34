#4. Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva


# Solicitar ao usuário que insira um número inteiro positivo
try:
    numero = int(input("Digite um número inteiro positivo: "))

    # Verificar se o número é positivo
    if numero <= 0:
        print("O número deve ser um inteiro positivo.")
    else:
        # Exibir a contagem regressiva
        print("Contagem regressiva:")
        for i in range(numero, -1, -1):
            print(i)
except Exception :
    print("Entrada inválida. Por favor, digite um número inteiro.")
