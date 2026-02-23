
from classes import GafanhotoDB
from os import getenv
from dotenv import load_dotenv

load_dotenv()

gafanhoto = GafanhotoDB()

gafanhoto.conectar(
    host=getenv("DB_HOST"), 
    user=getenv("DB_USER"), 
    password=getenv("DB_PASS"), 
    database=getenv("DB_NAME")
)

print(gafanhoto.listar())
