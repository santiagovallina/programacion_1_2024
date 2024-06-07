# Santiago Vallina

# Ejercicio 1: El almacén de barrio nos pide un programa para almacenar, ordenar y
# controlar stock de su mercadería por día.
# Comienza el día con la siguiente disposición en su góndola:
# Cada celda (fila/columna) muestra la ubicación de cada producto, ejemplo: en (1,2)
# se guardan las botellas, etc.
# Armar la lista de Productos con nombre, cantidad y ubicación (fila, columna)

gondola = [
    ["botellas", 3, [1, 2]],
    ["frascos", 8, [1, 4]],
    ["fideos", 4, [2, 3]],
    ["leche", 6, [3, 4]],
    ]


# 1-Alta de productos (producto nuevo)
def agregar_productos(lista_productos: list) -> list:
    '''
    Recibe por parámetro la lista que será modificada, pide el producto
    a agregar, la cantidad, y su posición.
    Guarda lo pedido en una lista y la agrega a la lista principal.
    Retorna la lista completa.
    '''
    producto = input("Ingrese el producto que desea agregar: ")
    cantidad = int(input("Ingrese la cantidad: "))
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    posicion = [fila, columna]
    nuevo_producto = [producto, cantidad, posicion]
    lista_productos.append(nuevo_producto)
    return lista_productos


# 2-Baja de productos (producto existente)
def eliminar_productos(lista_productos: list) -> list:
    '''
    Recibe por parámetro la lista a modificar y pide la posición que será eliminada.
    Elimina el elemento que se encuentra en esta posición. 
    Retorna la lista completa.
    '''
    posicion = int(input("Ingrese el número de índice que desea eliminar: "))
    lista_productos.pop(posicion)
    return lista_productos


# 3-Modificar productos (cantidad, ubicación)
def modificar_productos(lista_productos: list) -> list:
    '''
    Recibe la lista por parámetro. Pide índice, cantidad y posición.
    Modifica el producto que se encuentra en ese índice, cambiando la cantidad
    y la posición.
    Retorna la lista completa.
    '''
    indice = int(input("Ingrese el número de índice que desea modificar: "))
    cantidad = int(input("Ingrese la cantidad que desea modificar: "))
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    posicion = [fila, columna]
    lista_productos[indice][1] = cantidad
    lista_productos[indice][2] = posicion
    return lista_productos


# 4-Listar productos
def listar_productos(lista_productos: list) -> str:
    '''
    Recibe la lista por parámetro. La recorre mostrando cada elemento 
    de esta.
    Retorna un mensaje con el listado.
    '''
    print("Lista de Productos:")
    for producto in lista_productos:
        nombre = producto[0]
        cantidad = producto[1]
        ubicacion = producto[2]
        listado = print(f"Producto: {nombre}, Cantidad: {cantidad}, Ubicación: {ubicacion}")
    return listado


# 5-Lista de productos ordenado por nombre
def ordenar_por_nombre(lista_productos):
    '''
    Recibe la lista. La ordena por nombre.
    Retorna la lista ordenada.
    '''
    for i in range(len(lista_productos) - 1):
        for j in range(i + 1,(len(lista_productos))):
            if lista_productos[i] > lista_productos[j]:
                aux_lista_productos = lista_productos[i]
                lista_productos[i] = lista_productos[j]
                lista_productos[j] = aux_lista_productos
    return lista_productos











