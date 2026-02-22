'''
Faça uma lista com todos os 
dados de todas as mulheres que 
nasceram no Brasil e que tem o seu 
nome iniciado com a letra J
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
    SELECT *
    FROM gafanhotos
    WHERE 
        sexo = 'F' AND 
        nacionalidade = 'Brasil' AND 
        nome LIKE 'J%';
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt='grid')
print(tabela)