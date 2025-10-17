from src.model.pedido import Pedido, ItemPedido

class ControllerPedido:
    def __init__(self):
        self.pedidos = []      # Lista com todos os pedidos
        self.proximo_id = 1
        
    def criar_pedido(self,cliente):
        # Cria um novo pedido vazio para o cliente
        pedido = Pedido(self.proximo_id, cliente)
        self.pedidos.append(pedido)
        self.proximo_id+= 1
        return pedido
    def listar_pedidos(self):
        # Lista todos os pedidos
        if not self.pedidos:
            print("⚠️ Nenhum pedido foi realizado ainda")
            return
        for p in self.pedidos:
            print (p)
            print("-" * 50)

    def buscar_pedido_por_id(self, id_pedido):
        #procura um pedido pelo ID
        for p in self.pedidos:
            if p.id_pedido == id_pedido:
                return p
        return None