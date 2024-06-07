# Santiago Vallina
# Desarrollar un programa para el control de stock de una ferretería para
# sus artículos de tornillos y tarugos. Los mismos se encuentran almacenados en una
# cajonera de ferretería metálica con cajones.

estanteria = [
    ["to12", 65], ["to16", 86], ["to20", 65], ["to25", 45],
    ["to30", 68], ["to35", 73], ["to40", 85], ["to45", 89],
    ["ta4", 58], ["ta5", 48], ["ta6", 64], ["ta7", 96],
    ["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71],
]

# 1- Reponer mercadería (productos existentes)
def reponer_mercaderia(lista_estanteria: list) -> list:
    '''
    Recibe una lista. Pide un producto y una cantidad.
    Si el producto se encuentra en la lista, suma la cantidad 
    al digito que se encuentra en esa posición.
    Retorna la lista actualizada.
    '''
    producto = input("Ingrese el índice del producto que desea reponer: ")
    cantidad = int(input("Ingrese la cantidad que desea agregar: "))
    for fila in lista_estanteria:
        if fila[0] == producto:
            fila[1] += cantidad
    return lista_estanteria


# 2- Vender mercadería (producto existente, solo si alcanza el stock)
def vender_mercaderia(lista_estanteria):
    '''
    Recibe una lista. Pide producto y cantidad. Si el producto
    se encuentra en la lista, le resta la cantidad obtenida.
    Retorna la lista actualizada.
    '''
    producto = input("Ingrese el producto a vender: ")
    cantidad = int(input("Ingrese la cantidad: "))
    stock = False
    while not stock:
        for fila in lista_estanteria:
            if fila[0] == producto:
                stock = True
                if fila[1] >= cantidad:
                    fila[1] -= cantidad
                else:
                    print("No hay tantos elementos")
                    cantidad = int(input("Ingrese la cantidad nuevamente: "))
                    stock = False
    return lista_estanteria


# 3- Listar inventario
def listar_productos(lista_estanteria: list) -> str:
    '''
    Recibe la lista por parámetro. La recorre mostrando cada elemento 
    de esta.
    Retorna un mensaje con el listado.
    '''
    print("Lista de Productos:")
    for producto in lista_estanteria:
        nombre = producto[0]
        cantidad = producto[1]
        listado = print(f"Producto: {nombre}, Cantidad: {cantidad}")
    return listado


