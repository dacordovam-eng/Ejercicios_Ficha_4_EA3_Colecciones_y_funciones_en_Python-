
#Funcion sin parametros ni retorno
def Opciones_menu():
    print('''\n
========== MENÚ PRINCIPAL ==========
1. Agregar producto
2. Buscar producto
3. Eliminar producto
4. Actualizar disponibilidad
5. Mostrar productos
6. Salir
=====================================
\n''')

#Funcion con parametros y con retorno
def Seleccion_Opcion_Menu():
    while True:
        try:
            Num_Opcion_menu = int(input("\u274c | Ingrese un número de opción de Menú: "))
            if 1 <= Num_Opcion_menu <= 6:
                return Num_Opcion_menu
            print("\u274c | ¡Error! Ingrese un número entre 1 y 6 del menú")
        except ValueError:
            print("\u274c | ¡Error! Ingrese solo números disponibles en Menú de Opciones ")

#Funcion con parametros y con retorno 
def Validacion_Nombre(Nombre_Valido):
    if Nombre_Valido.strip() == "":
        return False
    return True

#Funcion con parametros y con retorno
def Validacion_Precio(Precio_Valido):
    try:
        Precio_Valido = float(Precio_Valido)
        if Precio_Valido > 0:
            return True
        return False
    except ValueError:
        print('''\u274c | ¡Error! Ingrese solo números para agregar precio''')

#Funcion con parametros y con retorno
def Validacion_Stock(Stock_Valido):
    try:
        Stock_Valido = int(Stock_Valido)
        if Stock_Valido >= 0:
            return True
        return False
    except ValueError:
        print("\u274c | ¡Error! Ingrese solo números para agregar Stock")
