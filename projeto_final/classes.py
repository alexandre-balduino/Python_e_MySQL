
from mysql.connector import connect

class GafanhotoDB:
    def __init__(self, host, user, password, database):
        from mysql.connector import connect
        self.conexao = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()
    
    
    def listar(self):
        self.cursor.execute('''
            SELECT nome
            FROM gafanhotos
        ''')
        resultado = []
        for tupla in self.cursor.fetchall():
            for nome in tupla:
                resultado.append(nome)
        return resultado
    
    
    def cadastrar(self):
        self.cursor.execute('''
            INSERT INTO gafanhotos
            VALUES ();
        ''')


