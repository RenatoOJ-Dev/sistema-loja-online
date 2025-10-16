# src/main.py

from src.controller.controller_cliente import ControllerCliente
from src.controller.controller_produto import ControllerProduto
from src.model.cliente import Cliente
from src.model.produto import Produto

def menu_principal():
    controller_cliente = ControllerCliente()
    controller_produto = ControllerProduto()

    while True:
        print("\n===== SISTEMA DE LOJA ONLINE =====")
        print("1 - Menu de Clientes")
        print("2 - Menu de Produtos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(controller_cliente)
        elif opcao == "2":
            menu_produtos(controller_produto)
        elif opcao == "3":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")


def menu_clientes(controller):
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Remover cliente")
        print("5 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            controller.inserir(Cliente(None, nome, email, telefone, endereco))
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            id_cliente = int(input("ID: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            endereco = input("Novo endereço: ")
            controller.atualizar(Cliente(id_cliente, nome, email, telefone, endereco))
        elif opcao == "4":
            id_cliente = int(input("ID a remover: "))
            controller.remover(id_cliente)
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


def menu_produtos(controller):
    while True:
        print("\n--- MENU PRODUTOS ---")
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("5 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))
            controller.inserir(Produto(None, nome, categoria, preco))
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            id_produto = int(input("ID: "))
            nome = input("Novo nome: ")
            categoria = input("Nova categoria: ")
            preco = float(input("Novo preço: "))
            controller.atualizar(Produto(id_produto, nome, categoria, preco))
        elif opcao == "4":
            id_produto = int(input("ID a remover: "))
            controller.remover(id_produto)
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
