'''
#################### LOGIN o REGISTRO ###################

Módulo que contiene las funciones tanto para login de usuarios como para el registro de usuarios (sólo externos)
Para usuarios internos sólo se contemplan los que se encuentran en el arhivo JSON ya que se busca simular que los usuarios internos sólo pueden ser generados por un perfil específico de la empresa.
'''

import os, json, re


usuarios_registrados = []  # Lista vacía para almacenar los usuarios registrados

def cargar_usuarios():
    '''
    Carga los usuarios que se encuentran en el archivo JSON.
    '''
    global usuarios_registrados
    archivo_json = 'usuarios.json'
    if os.path.isfile(archivo_json):
        with open(archivo_json) as file:
            usuarios_registrados = json.load(file)

def guardar_usuarios():
    '''
    Guarda los usuarios que se encuentran en el archivo JSON una vez se realizan las funciones del CRUD.
    '''
    archivo_json = 'usuarios.json'
    with open(archivo_json, 'w') as file:
        json.dump(usuarios_registrados, file)

def iniciar_sesion():
    '''
    Función que controla el inicio de sesión de los usuarios. Se valida que el usuario exista en nuestro archivo JSON y que la contraseña sea conincidente con la de nuestro archivo.
    '''
    while True:
            username = input("Usuario: ")
            password = input("Contraseña: ")

            # Verificar si el usuario existe
            usuario_existente = next((usuario for usuario in usuarios_registrados if usuario['username'] == username), None)
            if usuario_existente is None:
                os.system('cls')
                print("El usuario no existe.\n")
                return None

            # Verificar si la contraseña es correcta
            elif usuario_existente['password'] != password:
                print("La contraseña es incorrecta.\n")
                return None

            return username

def registrarse():
    '''
    Función que controla el registro de los usuarios. Se valida que el usuario no exista en nuestro archivo JSON, que se respeten el formato de nombre de usuario, que no aparezca en los registros.
    Finalmente se agrega el nuevo usuario por medio de la función append()
    '''
    os.system('cls')
    print(' REGISTRO DE USUARIO '.center(40,'#'))
    print(' Debe contener 4 letras y 2 dígitos \n(Ej: AbCd12) '.center(40,'#'))
    while True:
        nombre = input("Nombre: ").capitalize()
        apellido = input("Apellido: ").capitalize()
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        email = input("Mail: ")
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        if any(usuario['username'] == username for usuario in usuarios_registrados):
            print("El nombre de usuario ya está en uso. Por favor, elige otro.")
        elif re.search(r'[!@#$%^&*(),.?":{}|<>]', username):
            print("El nombre de usuario no puede contener caracteres especiales. Por favor, elige otro.")
        elif not re.search(r'^[A-Z a-z]{4}\d{2}$', username):
            print("El nombre de usuario debe contener al menos 4 letras y finalizar con 2 dígitos. Por favor, elige otro.")
        else:
            nuevo_usuario = {
                'nombre': nombre,
                'apellido': apellido,
                'dni': dni,
                'telefono': telefono,
                'email': email,
                'username': username,
                'password': password
            }

            usuarios_registrados.append(nuevo_usuario)
            guardar_usuarios()
            os.system('cls')
            print("Registro exitoso. Ahora puedes iniciar sesión.")
            return True