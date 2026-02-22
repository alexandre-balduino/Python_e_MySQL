'''
Faça uma lista com os dados de 
todos os gafanhotos que nasceram 
entre 01 de Janeiro de 2000 e 
31 de Dezembro de 2015
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
    SELECT *
    FROM gafanhotos
    WHERE nascimento BETWEEN '2000-01-01' AND '2015-12-31';
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
print(tabela)