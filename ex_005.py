'''
Faça uma lista com nome e 
nacionalidade de todos os homens que 
tem Silva no nome, não nasceram no 
Brasil e que tem menos de 100Kg
'''

from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect
from tabulate import tabulate

load_dotenv()

conexao = connect(
    host=getenv("DB_HOST"),
    user=getenv("DB_USER"),
    password=getenv("DB_PASS"),
    database=getenv("DB_NAME")
)
cursor = conexao.cursor()

cursor.execute('''
    SELECT nome, nacionalidade 
    FROM gafanhotos 
    WHERE sexo = 'M' AND nome LIKE  '%Silva%' AND nacionalidade != 'Brasil' AND peso < 100;
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
print(tabela)
