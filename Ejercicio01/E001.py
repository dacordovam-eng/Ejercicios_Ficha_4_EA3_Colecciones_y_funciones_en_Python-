
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
            Num_Opcion_menu = int(input("Ingrese un número de opción de Menú: "))
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
            return False
    
#Funcion con parametros y con retorno
def Validacion_Stock(Stock_Valido):
        try:
            Stock_Valido = int(Stock_Valido)
            if Stock_Valido >= 0:
                return True
            return False
        except ValueError:
            return False
        
#
def Agregar_Productos(Inventario):
   print("\n--------- AGREGAR NUEVO PRODUCTO ----------\n")
   Nombre = input("\tIngrese nombre de producto: ")
   Precio = input("\tIngrese precio de producto: ")
   Stock = input("\tIngrese el numero disponible de producto en stock: ")

   if not Validacion_Nombre(Nombre):
        print('''\u274c | ¡Error! El nombre no puede estar vacío ni ser solo espacios en blanco.
        =======================================================================================''')
        return
   if not Validacion_Precio(Precio):
        print('''\u274c | ¡Error! El precio debe ser un número decimal mayor que cero.
        =============================================================================''')
        return
   
   if not Validacion_Stock(Stock):
        print('''\u274c | ¡Error! El stock debe ser un número entero mayor o igual a cero.
        =================================================================================''')
        return

   Producto = {
       "Nombre": Nombre.strip(),
       "Precio": float(Precio),
       "Stock": int(Stock),
       "Disponible": False 
   }
   Inventario.append(Producto)
   print("\u2705\t| Producto agregado con exito.")
    

Inventario = []

while True:
    Opciones_menu()
    Opcion = Seleccion_Opcion_Menu()
    if Opcion == 1:
        Agregar_Productos(Inventario)
    elif Opcion == 2:
        print("")
    elif Opcion == 3:
        print("")
    elif Opcion == 4:
        print("")
    elif Opcion == 5:
        print("")
    elif Opcion == 6:
        print('''\nGracias por usar el sistema de inventario. Hasta pronto\n
                   =======================================================''')
        break
    else:
        print("\u274c | ¡Error! Ingrese un numero de opcion valido en el menú")
    


