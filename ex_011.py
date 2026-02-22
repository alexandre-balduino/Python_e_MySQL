'''
Quantos gafanhotos homens e 
mulheres nasceram após 
01/Janeiro/2005?
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
    SELECT sexo, COUNT(*)
    FROM gafanhotos
    WHERE nascimento > '2005-01-01'
    GROUP BY sexo;
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt="grid")
print(tabela)
