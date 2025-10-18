# src/controller/controller_relatorios.py

class ControllerRelatorios:
    def __init__(self, controller_pedido):
        # Recebe o controlador de pedidos, que contém a lista de pedidos
        self.controller_pedido = controller_pedido

    def vendas_por_cliente(self):
        """Mostra o total de vendas de cada cliente."""
        if not self.controller_pedido.pedidos:
            print("⚠️ Nenhum pedido registrado.")
            return

        totais = {}
        for pedido in self.controller_pedido.pedidos:
            nome = pedido.cliente.nome
            totais[nome] = totais.get(nome, 0) + pedido.total

        print("\n💰 Total de vendas por cliente:")
        print("-----------------------------------")
        for nome, total in totais.items():
            print(f"{nome}: R${total:.2f}")
        print("-----------------------------------")

    def vendas_por_produto(self):
        """Mostra o total vendido de cada produto."""
        if not self.controller_pedido.pedidos:
            print("⚠️ Nenhum pedido registrado.")
            return

        totais = {}
        for pedido in self.controller_pedido.pedidos:
            for item in pedido.itens:
                nome_produto = item.produto.nome
                totais[nome_produto] = totais.get(nome_produto, 0) + item.quantidade

        print("\n📦 Quantidade vendida por produto:")
        print("-----------------------------------")
        for nome, qtd in totais.items():
            print(f"{nome}: {qtd} unidade(s)")
        print("-----------------------------------")

    def faturamento_total(self):
        """Mostra o faturamento total da loja."""
        if not self.controller_pedido.pedidos:
            print("⚠️ Nenhum pedido registrado.")
            return

        total = sum(p.total for p in self.controller_pedido.pedidos)
        print("\n💵 Faturamento total da loja:")
        print("-----------------------------------")
        print(f"Total geral de vendas: R${total:.2f}")
        print("-----------------------------------")
