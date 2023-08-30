agenda = {}

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o número de telefone do contato: ")
    agenda[nome] = numero
    print("Contato inserido com sucesso!")

def exibir_contatos():
    if len(agenda) == 0:
        print("A agenda está vazia.")
    else:
        print("Lista de contatos:")
        for nome, numero in agenda.items():
            print(f"Nome: {nome}, Número: {numero}")

def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")
    if nome in agenda:
        novo_numero = input("Digite o novo número de telefone: ")
        agenda[nome] = novo_numero
        print("Contato editado com sucesso!")
    else:
        print("Contato não encontrado na agenda.")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado na agenda.")

def main():
    while True:
        print("\nAgenda Telefônica")
        print("1. Inserir Contato")
        print("2. Exibir Contatos")
        print("3. Editar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            inserir_contato()
        elif escolha == "2":
            exibir_contatos()
        elif escolha == "3":
            editar_contato()
        elif escolha == "4":
            remover_contato()
        elif escolha == "5":
            print("Saindo da agenda.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
