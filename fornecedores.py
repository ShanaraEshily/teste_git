
fornecedores = []

def cadastrar_fornecedor():
    nome = input("Nome do fornecedor: ")
    cnpj = input("CNPJ: ")

    fornecedor = {
        "nome": nome,
        "cnpj": cnpj
    }

    fornecedores.append(fornecedor)
    print("Fornecedor cadastrado com sucesso!")

def listar_fornecedores():
    print("\n--- Fornecedores ---")

    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
    else:
        for fornecedor in fornecedores:
            print(f"Nome: {fornecedor['nome']}")
            print(f"CNPJ: {fornecedor['cnpj']}")
            print("-------------------")

while True:
    print("\n=== Cadastro de Fornecedores ===")
    print("1 - Cadastrar fornecedor")
    print("2 - Listar fornecedores")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_fornecedor()
    elif opcao == "2":
        listar_fornecedores()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
