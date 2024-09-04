#12. Crie um programa que traduza qualquer texto em qualquer idioma para o português.


from googletrans import Translator, LANGUAGES

def traduzir_para_portugues(texto, idioma_origem):
    translator = Translator()
    traducao = translator.translate(texto, src=idioma_origem, dest='pt')
    return traducao.text

def main():
    print("Bem-vindo ao tradutor para o português!")

    # Exibir os idiomas suportados
    print("\nIdiomas suportados:")
    for codigo, nome in LANGUAGES.items():
        print(f"{codigo}: {nome}")

    idioma_origem = input("\nDigite o código do idioma de origem (ex: 'en' para inglês, 'es' para espanhol): ").strip()
    texto = input("Digite o texto a ser traduzido: ")

    try:
        resultado = traduzir_para_portugues(texto, idioma_origem)
        print(f"\nTexto traduzido para o português:\n{resultado}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
