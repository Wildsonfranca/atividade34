#10.  Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.

# Função para cadastrar cursos
def cadastrar_cursos():
    cursos = []
    
    print("Cadastro de Cursos")
    
    while True:
        nome_curso = input("Digite o nome do curso: ")
        
        while True:
            try:
                duracao = float(input("Digite a duração do curso em horas: "))
                if duracao <= 0:
                    print("A duração deve ser um número positivo. Tente novamente.")
                    continue
                break
            except Exception :
                print("Entrada inválida. Por favor, digite um número válido para a duração.")
        
        periodo_dia = input("Digite o período do dia (Manhã/Tarde/Noite): ").strip().capitalize()
        while periodo_dia not in ["Manhã", "Tarde", "Noite"]:
            print("Período do dia inválido. Escolha entre Manhã, Tarde ou Noite.")
            periodo_dia = input("Digite o período do dia (Manhã/Tarde/Noite): ").strip().capitalize()
        
        while True:
            try:
                vagas = int(input("Digite a quantidade de vagas: "))
                if vagas <= 0:
                    print("A quantidade de vagas deve ser um número positivo. Tente novamente.")
                    continue
                break
            except Exception :
                print("Entrada inválida. Por favor, digite um número inteiro para a quantidade de vagas.")
        
        cursos.append({
            "Nome": nome_curso,
            "Duração (horas)": duracao,
            "Período do dia": periodo_dia,
            "Quantidade de vagas": vagas
        })
        
        continuar = input("Deseja cadastrar outro curso? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    return cursos

# Função para exibir cursos
def exibir_cursos(cursos):
    print("\nCursos Cadastrados:")
    for i, curso in enumerate(cursos, start=1):
        print(f"\nCurso {i}:")
        print(f"Nome: {curso['Nome']}")
        print(f"Duração (horas): {curso['Duração (horas)']}")
        print(f"Período do dia: {curso['Período do dia']}")
        print(f"Quantidade de vagas: {curso['Quantidade de vagas']}")

# Programa principal
def main():
    cursos = cadastrar_cursos()
    exibir_cursos(cursos)

if __name__ == "__main__":
    main()

