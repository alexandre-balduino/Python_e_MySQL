'''
Faça uma lista com o nome de 
todas as gafanhotas mulheres
'''

import os
import mysql.connector 
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

conexao = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_name
)

cursor = conexao.cursor()

cursor.execute('''
    SELECT nome 
    FROM gafanhotos
    WHERE sexo = 'F';
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
print(tabela)
