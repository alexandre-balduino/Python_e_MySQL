'''
Faça uma lista com o nome de 
todos os homens que trabalham como 
programadores
'''

from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect
from tabulate import tabulate

load_dotenv()

db_host = getenv("DB_HOST")
db_user = getenv("DB_USER")
db_pass = getenv("DB_PASS")
db_name = getenv("DB_NAME")

conexao = connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_name
)
cursor = conexao.cursor()

cursor.execute('''
    SELECT nome 
    FROM gafanhotos
    WHERE sexo = 'M' AND profissao = 'Programador';
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
print(tabela)