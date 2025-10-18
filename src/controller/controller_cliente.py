from src.model.cliente import Cliente

class ControllerCliente:
    def __init__(self):
        # Aqui a lista vai simular uma tabela de clientes no banco
        self.clientes = []
        self.proximo_id = 1  # serve para simular o auto incremento do banco

    def inserir(self, cliente: Cliente):
        """Simula a inserção de um cliente"""
        cliente.id_cliente = self.proximo_id  # atribui um ID único
        self.clientes.append(cliente)          # adiciona à lista
        self.proximo_id += 1                   # prepara o próximo ID
        print("✅ Cliente inserido com sucesso!")
        return cliente # Retorna o objeto para que quem chamou possa usar/mostrar

    def listar(self):
        """Simula a listagem de clientes"""
        if not self.clientes:
            print("⚠️ Nenhum cliente cadastrado.")
            return
        print("\n📋 Lista de Clientes:")
        for c in self.clientes:
            print(f"ID: {c.id_cliente} | Nome: {c.nome} | Email: {c.email} | Telefone: {c.telefone} | Endereço: {c.endereco}")

    def remover(self, id_cliente, pedidos=[]):
        """Remove cliente somente se não houver pedidos associados"""
        for pedido in pedidos:
            if pedido.cliente.id_cliente == id_cliente:
                print("❌ Não é possível remover este cliente: há pedidos vinculados a ele.")
                return

        self.clientes = [c for c in self.clientes if c.id_cliente != id_cliente]
        print("✅ Cliente removido com sucesso!")

    def atualizar(self, cliente: Cliente):
        """Simula a atualização de dados de um cliente"""
        for c in self.clientes:
            if c.id_cliente == cliente.id_cliente:
                c.nome = cliente.nome
                c.email = cliente.email
                c.telefone = cliente.telefone
                c.endereco = cliente.endereco
                print("✏️ Cliente atualizado com sucesso!")
                return c
        return None
