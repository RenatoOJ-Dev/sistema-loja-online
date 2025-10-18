# import psycopg2  # Biblioteca que permite conectar o Python ao PostgreSQL

# # Classe responsável por gerenciar a conexão e execução de comandos SQL
# class Conexao:
#     def __init__(self):
#         # Quando a classe é criada, ainda não há conexão
#         self.conn = None
#         self.cursor = None

#     def conectar(self):
#         """Cria a conexão com o banco de dados"""
#         try:
#             # Aqui você coloca os dados do seu banco (ajuste a senha!)
#             self.conn = psycopg2.connect(
#                 dbname="loja_online",      # nome do banco criado no PostgreSQL
#                 user="postgres",           # usuário padrão
#                 password="sua_senha_aqui", # substitua pela sua senha
#                 host="localhost",          # endereço do servidor (localhost = seu PC)
#                 port="5432"                # porta padrão do PostgreSQL
#             )
#             self.cursor = self.conn.cursor()  # O cursor é quem executa os comandos SQL
#         except Exception as e:
#             print("Erro ao conectar ao banco:", e)

#     def desconectar(self):
#         """Fecha a conexão e o cursor"""
#         if self.cursor:
#             self.cursor.close()
#         if self.conn:
#             self.conn.close()

#     def executar(self, sql, valores=None):
#         """
#         Executa comandos SQL que modificam o banco (INSERT, UPDATE, DELETE)
#         """
#         try:
#             self.conectar()
#             self.cursor.execute(sql, valores)
#             self.conn.commit()  # salva as alterações
#         except Exception as e:
#             print("Erro ao executar comando SQL:", e)
#             self.conn.rollback()  # desfaz alterações se der erro
#         finally:
#             self.desconectar()

#     def consultar(self, sql, valores=None):
#         """
#         Executa comandos SQL que buscam dados (SELECT)
#         """
#         try:
#             self.conectar()
#             self.cursor.execute(sql, valores)
#             return self.cursor.fetchall()  # reto
#         except Exception as e:
#             print("Erro na consulta:", e)
#             return []  # retorna lista vazia se der erro
#         finally:
#             self.desconectar()