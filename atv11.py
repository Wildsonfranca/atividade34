#11. Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).

import math

# Função para calcular a área do quadrado
def area_quadrado(lado):
    return lado ** 2

# Função para calcular a área do círculo
def area_circulo(raio):
    return math.pi * (raio ** 2)

# Função para calcular a área do triângulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Função para calcular a área do trapézio
def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

# Função principal
def main():
    print("Escolha a figura geométrica para calcular a área:")
    print("1. Quadrado")
    print("2. Círculo")
    print("3. Triângulo")
    print("4. Trapézio")

    escolha = input("Digite o número da figura geométrica: ")
    
    if escolha == '1':
        lado = float(input("Digite o comprimento do lado do quadrado: "))
        print(f"A área do quadrado é: {area_quadrado(lado):.2f}")
    
    elif escolha == '2':
        raio = float(input("Digite o raio do círculo: "))
        print(f"A área do círculo é: {area_circulo(raio):.2f}")
    
    elif escolha == '3':
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"A área do triângulo é: {area_triangulo(base, altura):.2f}")
    
    elif escolha == '4':
        base_maior = float(input("Digite a base maior do trapézio: "))
        base_menor = float(input("Digite a base menor do trapézio: "))
        altura = float(input("Digite a altura do trapézio: "))
        print(f"A área do trapézio é: {area_trapezio(base_maior, base_menor, altura):.2f}")
    
    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")

if __name__ == "__main__":
    main()
