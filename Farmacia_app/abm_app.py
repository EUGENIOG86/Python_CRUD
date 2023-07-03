'''
############ FUNCIONES CRUD ############ 

Módulo que posee las funciones referidas al CRUD del programa.
'''

import os, json, re
from Farmacia_app.reportes_app import listar_stock
from Farmacia_app.styles_app import crud_stock

reportes_json = 'reportes.json'
reportes_stock = []

def cargar_producto():
    '''
    Carga los productos que se encuentran en nuestro archivo JSON.
    '''
    global reportes_stock

    if os.path.exists(reportes_json):
        with open(reportes_json) as report:
            reportes_stock = json.load(report)

def guardar_producto():
    '''
    Guarda los productos que se encuentran en nuestro archivo JSON.
    '''
    global reportes_stock
    with open(reportes_json, 'w') as report:
        json.dump(reportes_stock, report)

def create_producto():
    '''
    Función que se invoca para crear nuevos productos.
    Se establecen validaciones de formatos para los productos. 
    Al finalizar el registro se utiliza la función .append(nuevo_producto).
    Finalmente se guarda (guardar_producto()) el producto en nuestro JSON.
    '''
    global reportes_stock

    print(' ALTA DE PRODUCTO '.center(40, '#'))
    while True:
        print('\n### El formato de código debe ser AA9999 ###')
        codigo = input("\nCódigo: ")
        if not re.match(r'^[A-Z]{2}\d{4}$', codigo):
            print("\nSe debe respetar el formato indicado.\n")
            break
        producto = input("Producto: ").upper()
        origen = input("Origen:\n(1) Nacional\n(2) Importado\n»")

        while origen not in ['1', '2']:
            print("Especificar origen según las opciones.")
            origen = input("Origen:\n(1) Nacional\n(2) Importado\n»")

        cantidad = input("Cantidad: ")
        if not cantidad.isdigit():
            print("\nLa cantidad debe ser un valor numérico.\n")
            break
        laboratorio = input("Laboratorio: ").upper()
        especialidad = input("Especialidad: ").upper()

        if any(p['Código'] == codigo for p in reportes_stock):
            print("El código ya está registrado.")
        else:
            nuevo_producto = {
                'Código': codigo,
                'Producto': producto,
                'Origen': origen,
                'Cantidad': int(cantidad),
                'Laboratorio': laboratorio,
                'Especialidad': especialidad
            }

            reportes_stock.append(nuevo_producto)
            guardar_producto()  # Guardar los productos actualizados en el archivo JSON
            os.system('cls')
            print("Registro exitoso.\n")
            return nuevo_producto['Producto']

def modificar_stock():
    '''
    Se invoca para modificar productos.
    Esta función primero muestra el stock (listar_stock()) para poder visualizar los códigos que podremos modificar.
    Se establece validador para el código ingresado el cual debe coincidir con los códigos existentes. 
    Durante la función se reasignan valores.
    Finalmente se guardan los cambios (guardar_producto()) en nuestro JSON.
    Contempla Try-Except: FileNotFoundError.
    '''
    global reportes_stock
    try:
        listar_stock(reportes_stock)
        buscar_codigo = input('Ingrese el código del producto a modificar: ')
        for codigo in reportes_stock:
            if codigo["Código"] == buscar_codigo:
                print(codigo)
                print("Ingrese los datos o presione Enter para continuar")
            
                cantidad = input(f"Cantidad ({codigo['Cantidad']}): ")
                if cantidad == "":
                    cantidad = codigo["Cantidad"]
                
                laboratorio = input(f"Laboratorio ({codigo['Laboratorio']}): ")
                if laboratorio == "":
                    laboratorio = codigo["Laboratorio"]
                
                especialidad = input(f"Especialidad ({codigo['Especialidad']}): ")
                if especialidad == "":
                    especialidad = codigo["Especialidad"]
                
                producto = input(f"Producto ({codigo['Producto']}): ")
                if producto == "":
                    producto = codigo["Producto"]
                
                codigo["Cantidad"] = cantidad 
                codigo["Laboratorio"] = laboratorio.upper()
                codigo["Especialidad"] = especialidad.upper()
                codigo["Producto"] = producto.upper()

                print('Modificación exitosa')
                break
        else: 
            print('\nPor favor verifique los datos ingresados.\n')
            return
    except FileNotFoundError:
        print('\nNo se encuentra información para mostrar.')
        return
    guardar_producto()  # Guardar los productos actualizados en el archivo JSON
    return

def opcion_crud():
        '''
        Menú principal del CRUD. Se relaciona con las funciones: *create_producto *modificar_stock *baja_stock
        '''
        while True:
                crud_stock()
                opcion = input("» ")

                if opcion == "1":
                    create_producto()
                    input("\nPress any to continue »»»")
                    continue
                elif opcion == "2":
                    modificar_stock()
                    input("\nPress any to continue »»»")
                    continue
                elif opcion == "3":
                    baja_stock()
                    input("\nPress any to continue »»»")
                    continue
                elif opcion == "0":
                    break
                else:
                    print("Opción inválida. Por favor, reingrese.")

def baja_stock():
    '''
    Se invoca para bajar productos.
    Esta función primero muestra el stock (listar_stock()) para poder visualizar los códigos que podremos dar de baja.
    Se establece validador para el código ingresado el cual debe coincidir con los códigos existentes. 
    Finalmente se guardan los cambios (guardar_producto()) en nuestro JSON.
    Contempla Try-Except: FileNotFoundError.
    '''
    global reportes_stock
    try:
        listar_stock(reportes_stock)
        buscar_codigo = input('Ingrese el código del producto a eliminar: ')
        for codigo in reportes_stock:
            if codigo["Código"] == buscar_codigo:
                print(codigo)
                confirmar = input("¿Estás seguro de que quieres eliminar este producto? (s/n): ")
                if confirmar.lower() == "s":
                    reportes_stock.remove(codigo)  # Eliminar el producto de la lista    
                    guardar_producto()  # Guardar los productos actualizados en el archivo JSON
                    print("Modificación exitosa.")

    except FileNotFoundError:
        print('\nNo se encuentra información para mostrar.')
        return
    


