#7. Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.

# Inicializar uma lista vazia para armazenar os nomes
nomes = []

# Solicitar ao usuário que insira nomes
print("Digite nomes (digite 'fim' para terminar):")

while True:
    nome = input("Digite um nome: ")
    
    if nome.lower() == 'fim':
        break
    
    nomes.append(nome)

# Ordenar a lista de nomes em ordem alfabética
nomes.sort()

# Exibir a lista de nomes em ordem alfabética
print("\nLista de nomes em ordem alfabética:")
for nome in nomes:
    print(nome)

# Exibir o número de nomes digitados
print(f"\nNúmero de nomes digitados: {len(nomes)}")
