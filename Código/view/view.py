from extra.extra_functions import *

class View:
    #Se solicitan al usuario los datos individuales de una fecha.
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

    #Imprimir un mensaje.
    def print_message(self, message):
        print(message)

    #Imprimir menu y solicitar una opción.
    def request_menu_option(self):
        print("SOCIALEVENT S.A.")
        print("1. Consultar por fecha")
        print("2. Registrar reserva")
        print("3. Cancelar reserva")
        print("0. Salir")
        return input("Ingrese una opción: \n")
    
    #Se le solicita al usuario datos personales del cliente.
    def request_personal_data(self, message):
            clear_screen()
            personal_data = input(f"Ingrese el {message} del cliente: \n")
            return personal_data
    
    #Se realiza una validacion general.
    def request_verification(self, message):
        while True:
            clear_screen()
            self.print_message(message)
            verification = input("¿Es correcto? 1 = SI / 0 = NO\n")
            if verification == "1" or verification == "0":
                return verification
            else:
                self.print_message("Ingresa una opción correcta")
                self.print_message("Presione una tecla para continuar...")
                wait_key()

    #Se imprime la lista de clientes leida desde un archivo.
    def print_client_list(self, clients):
        client_counter = 1
        print("Lista de Clientes")
        for client in clients:
            print(f"{client_counter}. {client.__str__()}")
            client_counter += 1
        print("0. Crear nuevo cliente")

    #Se solicita un número de cliente.
    def request_client(self):
        return input("Ingrese el número del cliente: \n")
    
    #Se imprime la lista de los servicios de la empresa.
    def print_services_list(self, services):
        services_counter = 1
        print("Lista de Servicios")
        for service in services:
            print(f"{services_counter}. {service.__str__()}")
            services_counter += 1
        print("0. Finalizar Carga Servicios")

    #Se imprime la lista de servicios elegidos por el usuario.
    def print_chosen_services(self, services):
        print("Lista de Servicios")
        for service in services:
            print(f"{service.__str__()}")

    #Se solicita el número de servicio.
    def request_service(self):
        return input("Ingrese el número del servicio: \n")
    
    #Se imprimen las reservas existentes.
    def print_reservations(self, reservations):
        reservations_counter = 1
        if reservations:
            print("Reservas existentes")
        for data in reservations:
            dni, date, total = data
            print(f"{reservations_counter}. DNI: {dni} - Fecha: {date} - Total: ${total}")
            reservations_counter += 1
        print("0. Salir")

    #Se solicita el número de reserva.
    def request_index(self):
        return input("Ingrese el número de reserva que desea borrar:\n")