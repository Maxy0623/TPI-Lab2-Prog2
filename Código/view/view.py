from extra.extra_functions import *

class View:
    def request_date(self, message, format):
        while True:
            clear_screen()
            data = input(f"Ingrese el {message} de la reserva en formato {format}: \n")
            if data.isnumeric() and int(data) > 0:
                return data
            else:
                print("El dato debe ser un entero positivo")
                self.print_message("Presione cualquier tecla para continuar...")
                wait_key()
                continue
        
    def print_message(self, message):
        print(message)

    def request_menu_option(self):
        print("SOCIALEVENT S.A.")
        print("1. Consultar por fecha")
        print("2. Registrar reserva")
        print("3. Cancelar reserva")
        print("0. Salir")
        return input("Ingrese una opción: \n")