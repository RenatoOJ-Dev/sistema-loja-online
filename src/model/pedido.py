from dateTime import datetime

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto #produto selecionado (objeto produto)
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade #calcula o valor do item

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} - R${self.subtotal:.2f}"
    
class Pedido:
    def __init__(self, id_pedido=None, cliente=None, data=None):
        self.id_pedido = id_pedido
        self.cliente = cliente  #objeto cliente
        self.data = data or datetime.now()    #se não for passada, usa a data atual
        self.itens = []     #lista de ItemPedido
        self.total = 0.0        #valor total do pedido

    def adicionar_item(self,item: ItemPedido):
        #Adiciona um produto ao pedido e atualiza o total
        self.itens.append(item)
        self.total += item.subtotal

    def __str__ (self):
        itens_str = "\n".join([f" - {item}" for item in self.itens])
        return (
            f"Pedido #{self.id_pedido} - Cliente: {self.cliente.nome}\n"
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
            f"Itens:\n{itens_str}\n"
            f"Total: R${self.total:.2f}"
        )
    