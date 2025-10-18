# src/main.py
from src.controller.controller_cliente import ControllerCliente
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_pedido import ControllerPedido
from src.controller.controller_relatorios import ControllerRelatorios
from src.model.cliente import Cliente
from src.model.produto import Produto
from src.model.pedido import ItemPedido
from src.utils.splash_screen import splash_screen
from src.utils.validadores import ler_telefone, ler_numero_inteiro, ler_numero_decimal, formatar_telefone



def menu_principal():
    controller_cliente = ControllerCliente()
    controller_produto = ControllerProduto()
    controller_pedido = ControllerPedido()
    controller_relatorios = ControllerRelatorios(controller_pedido)

    while True:
        print("\n===== SISTEMA DE LOJA ONLINE =====")
        print("1 - Menu de Clientes")
        print("2 - Menu de Produtos")
        print("3 - Menu de Pedidos")
        print("4 - Relatórios")
        print("5 - Sair")

        print("\nDesenvolvido por:")
        print("👤 Kaynan de Oliveira Barbosa")
        print("👤 Rafael Covre Vilque")
        print("👤 Ricardo Cardeais")
        print("👤 Renato Oliveira de Jesus")
        print("👤 Yuri Gabriel Amorim dos Santos\n")

        print("Disciplina: Banco de Dados 2025/2")
        print("Professor: Howard Roatti")



        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(controller_cliente, controller_pedido)
        elif opcao == "2":
            menu_produtos(controller_produto, controller_pedido)
        elif opcao == "3":
            menu_pedidos(controller_pedido, controller_cliente, controller_produto)
        elif opcao == "4":
            menu_relatorios(controller_relatorios)
        elif opcao == "5":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida!")


def menu_clientes(controller, controller_pedido):
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Remover cliente")
        print("5 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            while True:
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = ler_telefone("Telefone (somente números, com DDD): ")
                telefone = formatar_telefone(telefone)  # Formata automaticamente
                endereco = input("Endereço: ")
                cliente_inserido = controller.inserir(Cliente(None, nome, email, telefone, endereco))

                print("\n✅ Cliente cadastrado com sucesso! Comprovante:")
                print("---------------------------------------------")
                print(cliente_inserido)
                print("---------------------------------------------")

                continuar = input("\nDeseja cadastrar outro cliente? (S/N): ").strip().upper()
                if continuar != "S":
                    break

        elif opcao == "2":
            controller.listar()

        elif opcao == "3":
            while True:
                id_cliente = int(input("ID do cliente a atualizar: "))
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = ler_telefone("Novo telefone (somente números, com DDD): ")
                telefone = formatar_telefone(telefone)
                endereco = input("Novo endereço: ")

                cliente_atualizado = controller.atualizar(Cliente(id_cliente, nome, email, telefone, endereco))

                if cliente_atualizado:
                    print("\n✅ Cliente atualizado com sucesso! Comprovante:")
                    print("---------------------------------------------")
                    print(cliente_atualizado)
                    print("---------------------------------------------")
                else:
                    print("❌ Cliente não encontrado para atualização.")

                continuar = input("\nDeseja atualizar outro cliente? (S/N): ").strip().upper()
                if continuar != "S":
                    break


        elif opcao == "4":
            while True:
                id_cliente = int(input("ID do cliente a remover: "))

        # Confirmação antes de excluir
                confirmar = input("Tem certeza que deseja remover este cliente? (S/N): ").strip().upper()
                if confirmar != "S":
                    print("❌ Remoção cancelada.")
                else:
                    controller.remover(id_cliente, controller_pedido.pedidos)
                    print("✅ Cliente removido com sucesso!")

                continuar = input("\nDeseja remover outro cliente? (S/N): ").strip().upper()
                if continuar != "S":
                    break


        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


def menu_produtos(controller, controller_pedido):
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
            preco = ler_numero_decimal("Preço: ")
            controller.inserir(Produto(None, nome, categoria, preco))
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            id_produto = ler_numero_inteiro("ID do produto: ")
            nome = input("Novo nome: ")
            categoria = input("Nova categoria: ")
            preco = float(input("Novo preço: "))
            controller.atualizar(Produto(id_produto, nome, categoria, preco))
        elif opcao == "4":
            id_produto = int(input("ID a remover: "))
            controller.remover(id_produto, controller_pedido.pedidos)
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")

def menu_pedidos(controller_pedido, controller_cliente, controller_produto):
    while True:
        print("\n--- MENU PEDIDOS ---")
        print("1 - Criar novo pedido")
        print("2 - Listar pedidos")
        print("3 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            controller_cliente.listar()     # Listar clientes
            id_cliente = int(input("Informe o ID do cliente: "))
            cliente = next((c for c in controller_cliente.clientes if c.id_cliente == id_cliente), None)
            
            if not cliente:
                print("❌ Cliente não encontrado.")
            
            pedido = controller_pedido.criar_pedido(cliente)

            while True:
                controller_produto.listar()
                id_produto = int(input("ID do produto (0 para finalizar): "))
                if id_produto == 0:
                    print("✅ Pedido finalizado!")
                    break

                produto = next((p for p in controller_produto.produtos if p.id_produto == id_produto), None)
                if not produto:
                    print("❌ Produto não encontrado.")
                    continue
                
                quantidade = int(input("Quantidade: "))
                pedido.adicionar_item(ItemPedido(produto, quantidade))

            print("\n✅ Pedido criado com sucesso! Resumo:")
            print("---------------------------------------------")
            print(pedido)
            print("---------------------------------------------")

        elif opcao == "2":
            print("Lista de pedidos:")
            print("---------------------------------------------")
            controller_pedido.listar_pedidos()
            print("---------------------------------------------")
        elif opcao == "3":
            break
        
        else:
            print("❌Opção inválida!")

def menu_relatorios(controller):
    while True:
        print("\n--- MENU RELATÓRIOS ---")
        print("1 - Vendas por cliente")
        print("2 - Vendas por produto")
        print("3 - Faturamento total")
        print("4 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            controller.vendas_por_cliente()
        elif opcao == "2":
            controller.vendas_por_produto()
        elif opcao == "3":
            controller.faturamento_total()
        elif opcao == "4":
            break
        else:
            print("❌ Opção inválida!")



if __name__ == "__main__":
    splash_screen()
    menu_principal()
