'''
#################### MENU ESTILIZADO ###################

Módulo que contiene los menú estilizados del programa.
Se utilizó para la generación de los mismos el código ASCII.
'''

def menu_principal():
    '''
    Función para mostrar menú estilizado.
    '''
    menu_main = print( '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Iniciar sesión     ║
    ║  [2] Registrarse        ║
    ╚═════════════════════════╝
    ''')
    
def menu_interno():
    '''
    Función para mostrar menú estilizado a los usuarios externos.
    '''
    menu_int = print(  '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Gestión de stock   ║
    ║  [2] Reportes           ║
    ║                         ║
    ║  [0] Salir              ║
    ╚═════════════════════════╝
    ''')
 
def crud_stock():
    '''
    Función para mostrar menú estilizado del CRUD.
    '''
    crud_stock = print(  '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ║≡≡≡≡  ABM Productos  ≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Alta               ║
    ║  [2] Modificación       ║
    ║  [3] Baja               ║
    ║                         ║
    ║  [0] Menú anterior      ║
    ╚═════════════════════════╝
    ''')

#Menú a realizar. Debería poder modificar según código de producto. Primero listar los productos. y dsp continuar con la modificación
def modificar_stock():
    '''
    Función para mostrar menú estilizado para UPDATE stock.
    '''
    modificar_stock = print(  '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ║≡  Modificar Productos  ≡║ 
    ╠═════════════════════════╣
    ║  [1] Especialidad       ║
    ║  [2] Origen             ║
    ║  [3] Cantidad en stock  ║
    ║                         ║
    ║  [0] Salir              ║
    ╚═════════════════════════╝
    ''')
    
#Menú realizado 100%  
def menu_externo():
    '''
    Función para mostrar menú estilizado a los usuarios externos.
    '''
    menu_ext = print(  '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Stock              ║
    ║  [2] Reportes           ║
    ║                         ║
    ║  [0] Salir              ║
    ╚═════════════════════════╝
    ''')

#Menú realizado 100%  
def submenu_productos():
    '''
    Función para mostrar menú estilizado dentro de la estructura de productos.
    '''
    submenu_prod = print(   '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║ 
    ║≡≡≡≡≡≡    Stock    ≡≡≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Productos en stock ║
    ║  [2] Últimos ingresos   ║
    ║  [3] Items Nacionales   ║
    ║  [4] Items Importados   ║
    ║                         ║
    ║  [0] Salir              ║
    ╚═════════════════════════╝
    ''')

#Menú realizado 100%   
def submenu_reportes():
    '''
    Función para mostrar menú estilizado dentro de la estructura de reportes.
    '''
    submenu_report = print( '''
    ╔═════════════════════════╗ 
    ║≡≡≡≡≡≡ FARMASTOCK® ≡≡≡≡≡≡║
    ║≡≡≡≡≡≡  Reportes   ≡≡≡≡≡≡║ 
    ╠═════════════════════════╣
    ║  [1] Por Laboratorio    ║
    ║  [2] Por especialidad   ║
    ║  [3] Nacionales         ║
    ║  [4] Importados         ║
    ║                         ║
    ║  [0] Salir              ║
    ╚═════════════════════════╝
    ''')


def msj_logout():
    '''
    Función para mostrar menú estilizado (Fin del Programa).
    '''
    msj_logout = print( '''
    ╔═════════════════════════════════╗
    ║≡≡≡≡≡≡ PROGRAMA FINALIZADO ≡≡≡≡≡≡║
    ║≡≡≡≡≡≡≡≡   FARMASTOCK®   ≡≡≡≡≡≡≡≡║ 
    ╚═════════════════════════════════╝
    ''')


