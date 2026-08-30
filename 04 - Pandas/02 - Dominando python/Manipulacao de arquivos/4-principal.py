from agenda import add_contacts, view_contacts, delete_contacts


def main():
    while True:
        print("\n1 - Adicionar contato")
        print("2 - Visualizar contatos")
        print("3 - Deletar contatos")
        print("4 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()