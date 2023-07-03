'''
#################### MAIN ###################

Módulo principal de programa.
'''
import os
from Farmacia_app.styles_app import menu_principal, menu_externo, menu_interno, msj_logout, submenu_productos, submenu_reportes, crud_stock
from Farmacia_app.login_app import iniciar_sesion, registrarse, cargar_usuarios
from Farmacia_app.reportes_app import opcion_reportes, opcion_productos
from Farmacia_app.abm_app import create_producto, cargar_producto, modificar_stock, opcion_crud, baja_stock

# Programa principal
cargar_usuarios() 
cargar_producto()

while True:
    menu_principal()
    opcion = input("» ")

    if opcion == "1":
        username = iniciar_sesion()
        if username:
            os.system('cls')
            print(f" Bienvenid@ {username} ".center(40, '#'))
            while True:
                if '.' in username:
                    menu_interno()
                    opcion_menu = input("» ")
                    if opcion_menu == "1":
                        while True:
                            crud_stock()
                            opcion_menu = input("» ")
                            if opcion_menu == "1":
                                    create_producto()
                                    input("\nPress any to continue »»»")
                            elif opcion_menu == "2":
                                modificar_stock()
                                opcion_crud()
                                break
                            elif opcion_menu == "3":
                                baja_stock()
                                opcion_crud()
                                break
                            elif opcion_menu == "0":
                                break
                            else:
                                print("Opción inválida. Por favor, selecciona una opción válida del menú.")

                    elif opcion_menu == "2":
                        submenu_reportes()
                        opcion_reportes()
                        break
                    elif opcion_menu == "0":
                        msj_logout()
                        break
                    else:
                        print("Opción inválida. Por favor, selecciona una opción válida del menú.")
                else:
                    menu_externo()
                    opcion_menu = input("» ")
                    if opcion_menu == "1":
                        submenu_productos()
                        opcion_productos()
                        break
                    elif opcion_menu == "2":
                        submenu_reportes()
                        opcion_reportes()
                        break
                    elif opcion_menu == "0":
                        msj_logout()
                        break
                    else:
                        print("Opción inválida. Por favor, selecciona una opción válida del menú.")
            break
    elif opcion == "2":
        if registrarse():
            continue
    else:
        print("Opción inválida. Por favor, selecciona 1 para iniciar sesión o 2 para registrarte.")
