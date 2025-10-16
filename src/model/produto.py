# Classe que representa a tabela PRODUTO no Python
class Produto:
    def __init__(self, id_produto=None, nome=None, categoria=None, preco=None):
        self.id_produto = id_produto   # chave primária
        self.nome = nome               # nome do produto
        self.categoria = categoria     # ex: Eletrônicos, Roupas
        self.preco = preco             # preço (decimal)

    def __str__(self):
        # Formata como o produto aparecerá na tela
        return f"[{self.id_produto}] {self.nome} ({self.categoria}) - R${self.preco:.2f}"
