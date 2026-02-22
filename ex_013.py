'''
Faça uma lista agrupada pela 
altura dos gafanhotos, mostrando 
quantas pessoas pesam mais de 100kg 
e que estão acima da média de 
altura de todos os cadastrados
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
    SELECT altura, COUNT(*)
    FROM gafanhotos
    WHERE peso > 100
    GROUP BY altura 
    HAVING altura > ( 
        SELECT AVG(altura) 
        FROM gafanhotos 
    );
''')

resultado = cursor.fetchall()
colunas = [c[0].upper() for c in cursor.description]
tabela = tabulate(resultado, headers=colunas, tablefmt="grid")
print(tabela)
