# Santiago Vallina
from biblioteca_stark import *

def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            print("¡Hasta luego!")
            return False


def mostrar_menu():
    '''
    Muestra el menú de opciones.
    Pide 
    '''
    menu = \
        """
        A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
        Nombre de manera ascendente.
        B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
        género M.
        C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de
        ojos.
        D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
        E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
        F. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
        género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género
        femenino
        G. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
        nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
        IMC calculado.
        H- Salir
        """
    
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ").upper()
        match opcion_elegida:
            case "A":
                orden_nombres = ordenar_iterable(copia_lista_personajes, "nombre", False)
                for i in orden_nombres:
                    print(i)
            case "B":
                print("Los héroes más débiles son:")
                for i, j in sacar_menor(copia_lista_personajes, "genero", "M", "fuerza", "nombre"):
                    print(f"Nombre: {j} ,Fuerza: {i}")
            case "C":
                print("Cantidad de héroes por color de ojos:") 
                for i, j in listar_cantidad_o_nombre_por_dato(copia_lista_personajes,
                    "color_ojos","nombre", False).items():
                    print(f"{i}: {j}")
            case "D":
                print("\nHéroes por color de pelo:")
                for i, j in listar_cantidad_o_nombre_por_dato(copia_lista_personajes,
                    "color_pelo","nombre", True).items():
                    print(f"{i}: {', '.join(j)}")
            case "E":
                print("\nHéroes por inteligencia:")
                for i, j in listar_cantidad_o_nombre_por_dato(copia_lista_personajes,
                    "inteligencia","nombre", True).items():
                    print(f"{i}: {', '.join(j)}")
            case "F":
                promedio = sacar_promedio(copia_lista_personajes, "genero", "F", "fuerza")
                print(f"El promedio de fuerza de las femeninas es: {promedio}")
                print("Estos son los datos de los heros con fuerza superior al promedio de las F")
                for i, j in mostrar_datos_mayores_al_promedio(copia_lista_personajes,"fuerza",
                "nombre","peso", "genero", "F",).items():
                    print(f"Héroe: {i}, peso: {j:.5}")
            case "G":
                print("Este es el índice de masa corporal:")
                for i in calcular_imc(copia_lista_personajes, "peso", "altura"):
                    print(i["imc"], i["nombre"])
            case "H":
                print("Hasta luego :)")
                break
        limpiar_consola()
        if opcion_continuar() == False:
            break
print(mostrar_menu())