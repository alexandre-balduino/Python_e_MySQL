
import mysql.connector

class GafanhotoDB:
    def __init__(self):
        self.conexao = None
        self.cursor = None
    
    
    def conectar(self, host, user, password, database):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            return True
        except mysql.connector.Error:
            return False
            
    
    
    def listar(self):
        if not self.cursor:
            return []
        else:
            self.cursor.execute('''
                SELECT nome
                FROM gafanhotos
            ''')
            return [item[0] for item in self.cursor.fetchall()]
    
    
    def cadastrar(self, nome):
        try:
            sql = "INSERT INTO gafanhotos (nome) VALUES (%s)"
            self.cursor.execute(sql, (nome,))
            self.conexao.commit()
            return True
        except mysql.connector.Error:
            return False
    
    
    def desconectar(self):
        if self.conexao and self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()

