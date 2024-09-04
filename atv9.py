#9. Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra.
#
import os
from datetime import datetime

# Função para cadastrar eventos
def cadastrar_eventos():
    eventos = []
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade de eventos que deseja cadastrar: "))
            if quantidade <= 0:
                print("Quantidade deve ser um número positivo. Tente novamente.")
                continue
            break
        except Exception:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    for _ in range(quantidade):
        nome_evento = input("Digite o nome do evento: ")
        while True:
            try:
                classificacao = int(input("Digite a classificação indicativa (idade mínima): "))
                if classificacao < 0:
                    print("A classificação indicativa não pode ser negativa. Tente novamente.")
                    continue
                break
            except Exception:
                print("Entrada inválida. Por favor, digite um número inteiro para a classificação indicativa.")
        
        eventos.append({
            "nome": nome_evento,
            "classificacao": classificacao
        })
    
    return eventos

# Função para inscrever o usuário em um evento
def inscrever_usuario(eventos):
    while True:
        nome_usuario = input("Digite seu nome: ")
        while True:
            try:
                idade_usuario = int(input("Digite sua idade: "))
                if idade_usuario < 0:
                    print("A idade não pode ser negativa. Tente novamente.")
                    continue
                break
            except Exception :
                print("Entrada ")
