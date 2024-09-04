#8. Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.

# Função para calcular a média de uma lista de números
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Solicitar ao usuário a quantidade de números que deseja inserir
try:
    quantidade = int(input("Digite a quantidade de números decimais (de 0 a 10): "))

    # Verificar se a quantidade está dentro do intervalo permitido
    if 0 <= quantidade <= 10:
        numeros = []
        
        # Solicitar ao usuário os números decimais
        for i in range(quantidade):
            while True:
                try:
                    numero = float(input(f"Digite o número decimal {i + 1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número decimal válido.")
        
        # Calcular e exibir a média
        media = calcular_media(numeros)
        print(f"A média dos números informados é: {media:.2f}")
    
    else:
        print("Quantidade fora do intervalo permitido. Por favor, digite um número entre 0 e 10.")

except Exception :
    print("Entrada inválida. Por favor, digite um número inteiro.")
