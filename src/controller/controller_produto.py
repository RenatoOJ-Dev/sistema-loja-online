# src/controller/controller_produto.py

from src.model.produto import Produto

class ControllerProduto:
    def __init__(self):
        # Lista que simula o banco de dados
        self.produtos = []
        self.proximo_id = 1  # Simula o autoincremento do banco

    def inserir(self, produto: Produto):
        """Simula a inserção de um produto"""
        produto.id_produto = self.proximo_id
        self.produtos.append(produto)
        self.proximo_id += 1
        print("✅ Produto inserido com sucesso!")

    def listar(self):
        """Lista todos os produtos"""
        if not self.produtos:
            print("⚠️ Nenhum produto cadastrado.")
            return
        print("\n📦 Lista de Produtos:")
        for p in self.produtos:
            print(f"ID: {p.id_produto} | Nome: {p.nome} | Categoria: {p.categoria} | Preço: R${p.preco:.2f}")

    def remover(self, id_produto):
        """Remove um produto pelo ID"""
        for p in self.produtos:
            if p.id_produto == id_produto:
                self.produtos.remove(p)
                print("🗑️ Produto removido com sucesso!")
                return
        print("❌ Produto não encontrado.")

    def atualizar(self, produto: Produto):
        """Atualiza os dados de um produto"""
        for p in self.produtos:
            if p.id_produto == produto.id_produto:
                p.nome = produto.nome
                p.categoria = produto.categoria
                p.preco = produto.preco
                print("✏️ Produto atualizado com sucesso!")
                return
        print("❌ Produto não encontrado para atualização.")
