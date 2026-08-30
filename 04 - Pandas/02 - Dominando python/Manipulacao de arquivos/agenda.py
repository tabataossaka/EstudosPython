import os


def add_contacts():
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    adress = input("Digite o endereço do contato: ")

    contact = f"Nome: {name}, Telefone: {phone}, Endereço: {adress}\n"

    with open("contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)


def view_contacts():
    if not os.path.exists("contatos.txt"):
        print("Nenhum contato encontrado.")
        return

    with open("contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()

    print("Lista de contatos")
    print(contacts)


def delete_contacts():
    if not os.path.exists("contatos.txt"):
        print("Nenhum contato encontrado.")
        return

    with open("contatos.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("Contatos deletados com sucesso.")