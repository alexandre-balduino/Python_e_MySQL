'''
Qual é o menor peso entre alunas 
mulheres que nasceram fora do 
Brasil entre 01 de Janeiro de 1990 
e 31 de Dezembro de 2000?
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
    SELECT MIN(peso)
    FROM gafanhotos
    WHERE 
        sexo = 'F' AND 
        nacionalidade != 'Brasil' AND 
        nascimento BETWEEN 
            '1990-01-01' AND 
            '2000-12-31';
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt="grid")
print(tabela)