#5. Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.


# Criar uma lista com 10 nomes
nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"
]

# Solicitar ao usuário que informe um número inteiro correspondente a um índice
try:
    indice = int(input("Digite um número inteiro correspondente a um índice (0-9): "))
    
    # Verificar se o índice está dentro do intervalo válido
    if 0 <= indice < len(nomes):
        # Exibir o nome correspondente ao índice informado
        print(f"O nome no índice {indice} é {nomes[indice]}.")
    else:
        print("Índice fora do intervalo. Por favor, digite um número entre 0 e 9.")
except Exception :
    print("Entrada inválida. Por favor, digite um número inteiro.")
