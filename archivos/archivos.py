'''
    "title": "QUEVEDO || BZRP Music Sessions #52",
    "views": 227192970,
    "length": 204,   
    "img_url": 
    "date":
'''

#LECTURA DE UN ARCHIVO
def parse_csv(nombre_archivo: str) -> list:
    lista = []
    with open(nombre_archivo, "r") as archivo:              
        for e_linea in archivo:
            lista.append(e_linea)
    return lista
# lista = []
# lista = parse_csv("data.csv")

