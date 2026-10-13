
tarefas = []

def cadastrar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Lista de Tarefas ---")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida!")
