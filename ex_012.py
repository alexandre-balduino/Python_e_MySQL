'''
Faça uma lista com os gafanhotos 
que nasceram fora do Brasil, 
mostrando o país de origem e o 
total de pessoas nascidos lá. 
Só nos interessam os países que 
tiverem mais de 3 gafanhotos com 
essa nascionalidade
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
    SELECT nacionalidade, COUNT(*) 
    FROM gafanhotos 
    WHERE nacionalidade != 'Brasil' 
    GROUP BY nacionalidade 
    HAVING COUNT(*) > 3; 
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt="grid")
print(tabela)
