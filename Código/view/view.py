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
    
    def request_personal_data(self, message):
            clear_screen()
            personal_data = input(f"Ingrese el {message} del cliente: \n")
            return personal_data
    
    def request_verification(self, message):
        while True:
            self.print_message(message)
            verification = input("¿Es correcto? 1 = SI / 0 = NO")
            if verification == "1" or verification == "0":
                return verification
            else:
                self.print_message("Ingresa una opción correcta")
                continue

    def print_client_list(self, clients):
        client_counter = 1
        print("Lista de Clientes")
        for client in clients:
            print(f"{client_counter}. {client.__str__()}")
        print("0. Crear nuevo cliente")

    def request_client(self):
        return input("Ingrese el número del cliente: \n")
    
    def print_services_list(self, services):
        services_counter = 1
        print("Lista de Servicios")
        for service in services:
            print(f"{services_counter}. {service.__str__()}")

    def request_service(self):
        return input("Ingrese el número del servicio: \n")