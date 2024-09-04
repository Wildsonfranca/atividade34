##2. Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.

while True:
    try:
        # Solicitar ao usuário que insira o peso do bebê em gramas
        peso = float(input("Digite o peso do bebê em gramas: "))
        
        # Verificar se o peso é positivo
        if peso <= 0:
            print("O peso deve ser um número positivo. Tente novamente.")
            continue
        
        # Verificar se o peso é menor que 2500 gramas
        if peso < 2500:
            print("O bebê precisa ficar internado.")
        else:
            print("O bebê está com o peso normal.")
        break
    except Exception as e:
        print("Entrada inválida. Certifique-se de digitar um número válido.")


# peso = int(input('Informe o peso do bebê em gramas:'))
#ternario em python
#print('O bebê esta liberado.'if peso >= 2500 else 'O bebê precisa)