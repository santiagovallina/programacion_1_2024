# Nombre : Santiago
# Apellido : Vallina

# La división de higiene está trabajando en un control de stock para productos sanitarios.
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
# obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
# unidades)
# 4. La marca y el Fabricante.

# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.

def controlar_stock():
    productos = []
    precios = []
    unidades = []
    fabricantes = []
    precio_barbijo_mas_caro = None
    unidades_barbijo_mas_caro = 0
    fabricante_barbijo_mas_caro = ""
    producto_mas_unidades = None
    fabricante_mas_unidades = ""
    contador_jabones = 0
    
    for i in range(5):
        producto = input("Ingrese entre barbijo, jabon y alcohol: ").lower()
        while producto != "barbijo" and producto !=  "jabon" and producto != "alcohol":
            producto = input("Error, ingrese nuevamente: ").lower()
        productos.append(producto)
        
        precio = int(input("Ingrese el valor entre 100 y 300: "))
        while precio < 100 and precio > 300:
            precio = int(input("Ingrese el valor nuevamente: "))
        precios.append(precio)
        
        unidad = int(input("Ingrese cuantas unidades: "))
        while unidad < 1 and unidad > 1000:
            unidad = int(input("Ingrese nuevamente: "))
        unidades.append(unidad)
        
        fabricante = input("Ingrese el fabricante: ")
        fabricantes.append(fabricante)
    
    for i in range(len(productos)):
        if productos[i] == "barbijo":
            if precio_barbijo_mas_caro == None or precio_barbijo_mas_caro < precios[i]:
                precio_barbijo_mas_caro = precios[i]
                fabricante_barbijo_mas_caro = fabricantes[i]
                unidades_barbijo_mas_caro = unidades[i]
        
        if producto_mas_unidades == None or producto_mas_unidades < unidades[i]:
            nombre_producto_mas_unidades = productos[i]
            fabricante_mas_unidades = fabricantes [i]
            
        if productos[i] == "jabon":
            contador_jabones += unidades[i]
        
        mensaje = print(f"""
                        el barbijo mas caro vale ${precio_barbijo_mas_caro}, su
                        fabricante es {fabricante_barbijo_mas_caro} y hay
                        {unidades_barbijo_mas_caro} unidades.
                        El item con más unidades es {nombre_producto_mas_unidades},
                        hay {producto_mas_unidades} unidades y su fabricante es 
                        {fabricante_mas_unidades}.
                        Hay {contador_jabones} jabones.
                        """)
    return mensaje

print(controlar_stock())


