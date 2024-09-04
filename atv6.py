#6. Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos.


# Função para verificar se um número é primo
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Criar uma lista com números de 1 a 20
numeros = list(range(1, 21))

# Encontrar e exibir os números primos
primos = [num for num in numeros if eh_primo(num)]

print('Números primos de 1 a 20:')
print(primos)
