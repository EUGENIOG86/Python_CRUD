
'''
############ REPORTES y STOCK ############ 

Módulo que posee las funciones referidas a la generación de reportes que se utilizarán a lo largo del programa.
'''

from Farmacia_app.styles_app import submenu_reportes, msj_logout, submenu_productos
import json
reportes_json = 'reportes.json'
reportes_stock = []

def opcion_reportes():
        '''
        Menú principal de reportes.
        Se vincula con las funciones: *submenu_reportes *laboratorio_stock *especialidad_stock *nacionales_stock *importados_stock.
        Contempla Try-Except: FileNotFoundError.
        '''
        try:
            while True:
                    submenu_reportes()
                    opcion = input("» ")

                    if opcion == "1":
                        laboratorio_stock(reportes_json)
                        input("\nPress any to continue »»»")
                        continue
                    elif opcion == "2":
                        especialidad_stock(reportes_json)
                        input("\nPress any to continue »»»")
                        continue
                    if opcion == "3":
                        nacionales_stock(reportes_json)
                        input("\nPress any to continue »»»")
                        continue
                    elif opcion == "4":
                        importados_stock(reportes_json)
                        input("\nPress any to continue »»»")
                        continue
                    if opcion == "0":
                        msj_logout()
                        break
                    else:
                        print("Opción inválida. Por favor, reingrese.")
        except FileNotFoundError:
            print('\nNo se encuentra información para mostrar.')
            msj_logout()
            
def laboratorio_stock(reportes_json):
    '''
    Imprime en pantalla los productos en stock organizados por laboratorio.
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)
        print("\n" + "#" * 10 + " LABORATORIO " + "#" * 10 + "\n")
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        print(" " * 1 + "| {:^15} | {:^15} | {:^10} |".format("Laboratorio", "Producto", "Cantidad"))
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        for reporte in reportes_stock:
            laboratorio = reporte.get('Laboratorio', '')
            producto = reporte.get('Producto', '')
            cantidad = reporte.get('Cantidad', '')
            print(" " * 1 + "| {:<15} | {:<15} | {:^10} |".format(laboratorio, producto, cantidad))
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")


def importados_stock(reportes_json):
    '''
    Imprime en pantalla los productos importados en stock.
    Sólo se muestra la información de *producto y *cantidad.
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)
        print("\n" + "#" * 10 + " IMPORTADOS " + "#" * 10 + "\n")
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
        print(" " * 1 + "| {:^10} | {:^10} |".format("Producto", "Cantidad"))
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
        for reporte in reportes_stock:
            origen = reporte.get('Origen', '')
            producto = reporte.get('Producto', '')
            cantidad = reporte.get('Cantidad', '')
            if origen == '2':
                print(" " * 1 + "| {:<10} | {:^10} |".format(producto, cantidad))
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")

def nacionales_stock(reportes_json):
    '''
    Imprime en pantalla los productos nacionales en stock.
    Sólo se muestra la información de *producto y *cantidad.
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)
        print("\n" + "#" * 10 + " NACIONALES " + "#" * 10 + "\n")
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
        print(" " * 1 + "| {:^10} | {:^10} |".format("Producto", "Cantidad"))
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
        for reporte in reportes_stock:
            origen = reporte.get('Origen', '')
            producto = reporte.get('Producto', '')
            cantidad = reporte.get('Cantidad', '')
            if origen == '1':
                print(" " * 1 + "| {:<10} | {:^10} |".format(producto, cantidad))
        print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")

def especialidad_stock(reportes_json):
    '''
    Imprime en pantalla los productos en stock según la especialidad.
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)
        print("\n" + "#" * 10 + " ESPECIALIDAD " + "#" * 10 + "\n")
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        print(" " * 1 + "| {:^15} | {:^15} | {:^10} |".format("Especialidad", "Producto", "Cantidad"))
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        for reporte in reportes_stock:
            especialidad = reporte.get('Especialidad', '')
            producto = reporte.get('Producto', '')
            cantidad = reporte.get('Cantidad', '')
            print(" " * 1 + "| {:<16} | {:<14} | {:^10} |".format(especialidad, producto, cantidad))
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
            

def opcion_productos():
    '''
    Menú principal de reportes.
    Se vincula con las funciones: *submenu_reportes *laboratorio_stock *especialidad_stock *nacionales_stock *importados_stock.
    Contempla Try-Except: FileNotFoundError.
    '''
    try:
        while True:
                submenu_productos()
                opcion = input("» ")

                if opcion == "1":
                    productos_stock(reportes_json)
                    input("\nPress any to continue »»»")
                    continue
                elif opcion == "2":
                    nuevos_stock(reportes_json)
                    input("\nPress any to continue »»»")
                    continue
                if opcion == "3":
                    nacionales_stock(reportes_json)
                    input("\nPress any to continue »»»")
                    continue
                elif opcion == "4":
                    importados_stock(reportes_json)
                    input("\nPress any to continue »»»")
                    continue
                if opcion == "0":
                    msj_logout()
                    break
                else:
                    print("Opción inválida. Por favor, reingrese.")
    except FileNotFoundError:
        print('\nNo se encuentra información para mostrar.')
        msj_logout()


def productos_stock(reportes_json):
    '''
    Imprime en pantalla los productos en stock.
    Sólo se muestra la información de *producto y *cantidad.
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)   
    print("\n" + "#" * 10 + " EN STOCK " + "#" * 10 + "\n")
    print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
    print(" " * 1 + "| {:^10} | {:^10} |".format("Producto", "Cantidad"))
    print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
    for reporte in reportes_stock:
        producto = reporte.get('Producto', '')
        cantidad = reporte.get('Cantidad', '')
        print(" " * 1 + "| {:<10} | {:^10} |".format(producto, cantidad))
    print(" " * 1 + "+" + "-" * 12 + "+" + "-" * 12 + "+")
        
def nuevos_stock(reportes_json):
    '''
    Imprime en pantalla los últimos (3) ingresos por medio del uso de la funcion reversed().
    Se estructura en formato de tablas.
    '''
    with open(reportes_json) as report:
        reportes_stock = json.load(report)
        print("\n" + "#" * 10 + " ULTIMOS INGRESOS " + "#" * 10 + "\n")
        print(" " * 2 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        print(" " * 2 + "| {:^15} | {:^10} |".format("Producto", "Cantidad"))
        print(" " * 2 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
        for reporte in reversed(reportes_stock[-3:]):
            producto = reporte.get('Producto', '')
            cantidad = reporte.get('Cantidad', '')
            print(" " * 2 + "| {:<15} | {:^10} |".format(producto, cantidad))
        print(" " * 2 + "+" + "-" * 17 + "+" + "-" * 12 + "+")


def listar_stock(reportes_stock):
    '''
    Función que trabaja con el archivo JSON.
    Se muestra en formato de tablas el stock o listado de existencias.
    Esta función forma parte de las funciones del CRUD a lo largo del programa.
    '''
    with open('reportes.json') as report:
        reportes_stock = json.load(report)
    print("\n" + "#" * 10 + " LISTADO EXISTENCIAS " + "#" * 10 + "\n")
    print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 17 + "+"  + "-" * 17 + "+" + "-" * 12 + "+")
    print(" " * 1 + "| {:<15} | {:<15} | {:<15} | {:^15} | {:^10} |".format("Código", "Laboratorio", "Especialidad", "Producto", "Cantidad"))
    print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")
    for reporte in reportes_stock:
        codigo = reporte.get('Código', '')
        laboratorio = reporte.get('Laboratorio', '')
        especialidad = reporte.get('Especialidad', '')
        producto = reporte.get('Producto', '')
        cantidad = reporte.get('Cantidad', '')
        print(" " * 1 + "| {:<15} | {:<15} | {:<15} | {:<15} | {:^10} |".format(codigo, laboratorio, especialidad, producto, cantidad))
        print(" " * 1 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 12 + "+")

