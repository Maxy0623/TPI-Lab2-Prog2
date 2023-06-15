#Para el controlador se importan modelos y vista. Ademas de otras librerías necesarias.
from view.view import View
from models.client import Client
from models.service import Service
from models.reservation import Reservation
from datetime import datetime, timedelta
from extra.extra_functions import *
import os

class Controller:
    #Constructor.
    def __init__(self):
        #Este atributo guarda la fecha en la cual se está ejecutando el programa en formato YYYY/MM/DD.
        self._today = datetime.now().date().strftime("%Y/%m/%d")
        #Se crea una instancia de la Vista para acceder a sus funciones.
        self._view = View()
        self._clients = []
        self._services = []
        self._reservations = []
        self._reserved_dates = []
        self.fill_services_list()

    #Validamos si la fecha está reservada en nuestro archivo de fechas reservadas.
    def is_date_reserved(self, date):
        #Abrimos el archivo en modo lectura y buscamos una coincidencia.
        with open(r"resources\reserved_dates.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == date:
                    #Si se encuentra una coincidencia devolvemos True.
                    return True
            #Si no encontramos coincidencia en ninguna linea devolvemos False.
            return False
    
    #Agregamos una fecha disponible elegida por el usuario al archivo de fechas reservadas.
    def add_date_to_file(self, date):
        with open(r"resources\reserved_dates.txt", "a") as file:
            file.write(date)

    #Validamos que los datos necesarios para formar una fecha sean correctos.
    def date_validation(self):
        while True:
            year = self._view.request_date("año" ,"YYYY")
            #El año debe tener una longitud de 4 caracteres.
            if len(year) == 4:
                break
            else:
                self._view.print_message("Ingrese el año en el formato solicitado")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()
                continue
        while True:
            month = self._view.request_date("mes", "MM")
            #El mes debe tener longitud de 2 y debe estar comprendido entre 1 y 12.
            if int(month) <= 12 and len(month) == 2:
                break
            else:
                self._view.print_message("Ingrese un mes valido (01 ~ 12)")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()
                continue
        while True:
            day = self._view.request_date("dia", "DD")
            #El dia no debe exceder los días maximos de cada mes.
            if month in ["01", "03", "05", "07", "08", "10", "12"]:
                    #El dia debe ser menor o igual al limite y debe ser de dos digitos (DD).
                    if int(day) <= 31 and len(day) == 2:
                        break
                    else:
                        self._view.print_message(f"El mes {month} solo tiene 31 días, asegurése de ingresar el dia en formato DD.")
                        self._view.print_message("Presione cualquier tecla para continuar...")
                        wait_key()
                        continue
            elif month in ["04", "06", "09", "11"]:
                    if int(day) <= 30 and len(day) == 2:
                        break
                    else:
                        self._view.print_message(f"El mes {month} solo tiene 30 días, asegurése de ingresar el dia en formato DD.")
                        self._view.print_message("Presione cualquier tecla para continuar...")
                        wait_key()
                        continue
            elif month == "02":
                    #En el caso de febrero, si el año elegido es divisible por 4, significa que es un año bisiesto y febrero tendria 29 dias.
                    #NO SE ESTAN CONSIDERANDO TODOS LOS CASOS DE AÑOS BISIESTOS Y NO BISIESTOS.
                    #Año normal: año no divisible por 4 / año divisible por 100 pero no por 400 (véase año 1900).
                    #Año bisiesto: año divisible por 4 pero no por por 100 / año divisible por 4 por 100 y por 400.
                    if int(year) % 4 == 0:
                        if int(day) <= 29 and len(day) == 2:
                            break
                        else:
                            self._view.print_message(f"Febrero en el año {year} solo tiene 29 días, asegurése de ingresar el dia en formato DD.")
                            self._view.print_message("Presione cualquier tecla para continuar...")
                            wait_key()
                            continue
                    else:
                        if int(day) <= 28 and len(day) == 2:
                            break
                        else:
                            self._view.print_message(f"Febrero en el año {year} solo tiene 28 días, asegurése de ingresar el dia en formato DD.")
                            self._view.print_message("Presione cualquier tecla para continuar...")
                            wait_key()
                            continue
        return year, month, day
    
    #Buscamos fechas proximas.
    def find_available_dates(self, date):
        #Se crea una instancia de la clase datetime a partir del parametro date.
        date_object = datetime.strptime(date, "%Y/%m/%d")
        #Se decrementa en 1 la fecha
        previous_date = date_object - timedelta(days = 1)
        #Se incrementa en 1 la fecha
        next_date = date_object + timedelta(days = 1)
        #Creamos lista de fechas reservadas
        with open(r"resources\reserved_dates.txt", "r") as file:
            reserved_dates = file.readlines()
            reserved_dates = [date.strip() for date in reserved_dates]
        #Contadores se inician en 1 porque ya hubo una repeticion para cada fecha.
        next_counter = 1
        previuous_counter = 1
        #Si la fecha siguiente o previa están en la lista generada por el archivo, se sigue incrementando o decrementando.
        while next_date.strftime("%Y/%m/%d") in reserved_dates:
            next_date += timedelta(days = 1)
            next_counter += 1
        while previous_date.strftime("%Y/%m/%d") in reserved_dates:
            previous_date -= timedelta(days = 1)
            previuous_counter += 1
        available_dates = [previous_date.strftime("%Y/%m/%d"), next_date.strftime("%Y/%m/%d")]
        #Se devuelve una lista con las dos fechas disponibles y ambos contadores.
        return available_dates, next_counter, previuous_counter

    #Incorporamos toda la funcionaluidad anterior y logramos consultar fechas disponibles.
    def consult_date(self):
        #Se pide la fecha por separado.
        year, month, day = self.date_validation()
        #Se arma un string con la fecha.
        date = f"{year}/{month}/{day}"
        date_object = datetime.strptime(date, "%Y/%m/%d")
        #Si la fecha no esta reservada se imprime disponible en caso contrario se buscan las mas proximas.
        if not self.is_date_reserved(date) and date_object > datetime.strptime(self._today, "%Y/%m/%d"):
            self._view.print_message("La fecha está disponible")
            self._view.print_message("Presione cualquier tecla para continuar...")
            wait_key()
        else:
            available_dates, next_counter, previous_counter = self.find_available_dates(date)
            #Si el contador next es mayor significa que iteró mas veces para encontrar una fecha válida por tanto se devuelve la otra fecha SOLAMENTE SI LA previous_date es mayor a la fecha de hoy.
            if next_counter > previous_counter and available_dates[0] > self._today:
                self._view.print_message(f"La fecha más proxima disponible es {available_dates[0]}")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()
            #Si el contador previous es mayor significa que tuvo más iteraciones asique se devuelve la otra fecha O si los contadores son distintos y previous_date es anterior a la fecha de hoy.
            elif previous_counter > next_counter or (available_dates[0] <= self._today and previous_counter != next_counter):
                self._view.print_message(f"La fecha más proxima disponible es {available_dates[1]}")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()
            #Si los contadores son iguales, solo hay que verificar que las fechas no sean anteriores a hoy.
            else:
                if available_dates[0] > self._today:
                    self._view.print_message(f"Las fechas mas próximas disponibles son {available_dates[0]} y {available_dates[1]}")
                    self._view.print_message("Presione cualquier tecla para continuar...")
                    wait_key()
                elif available_dates[0] <= self._today and available_dates[1] > self._today:
                    self._view.print_message(f"La fecha más proxima disponible es {available_dates[1]}")
                    self._view.print_message("Presione cualquier tecla para continuar...")
                    wait_key()
                else:
                    self._view.print_message(f"{date} no es una fecha válida")
                    self._view.print_message("Ingrese una fecha válida")
                    self._view.print_message("Presione cualquier tecla para continuar...")
                    wait_key()

    #Verificamos si el archivo está vacío.
    def is_file_empty(self, path):
        file_size = os.stat(path).st_size
        if file_size == 0:
            return True
        else:
            return False

    #Creamos un cliente y lo añadimos a la lista de clientes.     
    def create_client(self, path):
        while True:
            name = self._view.request_personal_data("nombre y apellido")
            dni = self._view.request_personal_data("DNI")
            message = f"Nombre y Apellido: {name} - DNI: {dni}"
            verification = self._view.request_verification(message)
            if verification == "1":
                client_data = f"{name};{dni}\n"
                with open(path, "a") as file:
                    file.write(client_data)
                client = Client(name, dni)
                return client
            else:
                self._view.print_message("Ingrese nuevamente por favor.")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()

    #Llenamos la lista de clientes con instancias de la clase Client.
    def fill_client_list(self):
        self._clients = []
        with open(r"resources\clients.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(";")
                client = Client(data[0], data[1])
                self._clients.append(client)

    #Guardamos la fecha elegida por el cliente.
    def register_reservation_date(self):
        while True:
            clear_screen()
            year, month, day = self.date_validation()
            date = f"{year}/{month}/{day}"
            if not self.is_date_reserved(date):
                self.add_date_to_file(f"{date}\n")
                return date
            else:
                self._view.print_message("La fecha no está disponible")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()

    #Guardamos el cliente con el que estamos operando. Se crea un cliente nuevo en caso de que no exista ninguno, y si no existe el cliente que quiere operar en la lista se crea.
    def register_reservation_client(self):
        while True:
            verificator = self.is_file_empty(r"resources\clients.txt")
            if verificator:
                print(self.is_file_empty(r"resources\clients.txt"))
                client = self.create_client(r"resources\clients.txt")
                return client
            else:
                self.fill_client_list()
                while True:
                    clear_screen()
                    self._view.print_client_list(self._clients)
                    option = self._view.request_client()
                    if option.isnumeric() and int(option) >= 1 and int(option) <= len(self._clients):
                        client = self._clients[int(option) - 1]
                        return client
                    elif option.isnumeric() and option == "0":
                        client = self.create_client(r"resources\clients.txt")
                        return client
                    else:
                        self._view.print_message("Ingrese una opción válida")
                        self._view.print_message("Presione una tecla para continuar...")
                        wait_key()

    #Llenamos la lista de servicios con instancias de la clase Service
    def fill_services_list(self):
        self._services = []
        with open(r"resources\services.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(";")
                service = Service(data[0], data[1])
                self._services.append(service)

    #Guardamos los servicios elegidos por el cliente en una lista.
    def register_reservation_services(self):
        chosen_services = []
        while True:
            clear_screen()
            self._view.print_services_list(self._services)
            option = self._view.request_service()
            if option.isnumeric() and int(option) >= 1 and int(option) <= len(self._services):
                chosen_service = self._services[int(option) - 1]
                chosen_services.append(chosen_service)
            elif option.isnumeric() and option == "0":
                return chosen_services
            else:
                self._view.print_message("Ingrese una opción válida")
                self._view.print_message("Presione un tecla para continuar...")
                wait_key()

    #Creamos una instancia de la clase Reservation, calculamos el total y mostramos la info por pantalla.
    def register_reservation(self):
        date = self.register_reservation_date()
        client = self.register_reservation_client()
        chosen_services = self.register_reservation_services()
        reservation = Reservation(client, date, chosen_services)
        reservation.calculate_total()
        clear_screen()
        self._view.print_chosen_services(chosen_services)
        self._view.print_message(f"Los servicios elegidos para la fecha {date}\nhacen un total de: ${reservation.get_total()}")
        self._view.print_message(f"La seña a abonar es de: ${reservation.get_advance_payment()}")
        line = f"{reservation.client.get_dni()};{reservation.get_date()};{reservation.get_total()}\n"
        with open(r"resources\reservations.txt", "a") as file:
            file.write(line)
        self._view.print_message("Presione cualquier tecla para continuar...")
        wait_key()

    #Leemos el archivo con nuestras reservas almacenadas y las guardamos en una lista.
    def read_reservations(self):
        with open(r"resources\reservations.txt", "r") as file:
            for line in file:
                data = line.strip().split(";")
                self._reservations.append(data)
    
    #Borramos una reserva, dando un mensaje de que fue borrada.
    def delete_reservation(self, index):
        deleted_reservation = self._reservations.pop(index - 1)
        with open(r"resources\reservations.txt", "w") as file:
            for data in self._reservations:
                file.write(";".join(data)+"\n")
        self._view.print_message(f"La reserva {deleted_reservation} ha sido borrada.")

    #Calculamos la diferencia de días entre la fecha actual y la fecha de la reserva.
    def calculate_diference(self, date):
        format = "%Y/%m/%d"
        today = datetime.strptime(self._today, format)
        date_formated = datetime.strptime(date, format)
        diference = date_formated - today
        return diference.days

    #Leemos el archivo con fechas reservadas y las guardamos en una lista.
    def read_reserved_dates(self):
        with open(r"resources\reserved_dates.txt" ,"r") as file:
            for line in file:
                date = line.strip()
                self._reserved_dates.append(date)

    #Borramos una fecha del archivo.
    def delete_date(self, index):
        deleted_date = self._reserved_dates.pop(index - 1)
        with open(r"resources\reserved_dates.txt" ,"w") as file:
            if self._reserved_dates:
                for date in self._reserved_dates:
                    file.write(date + "\n")
            else:
                file.write("")
        self._view.print_message(f"La fecha {deleted_date} ya está disponible de nuevo.")

    #Cancelamos una reserva existente y volvemos a poner como disponible la fecha de esa reserva.
    def cancel_reservation(self):
        self._reservations = []
        self.read_reservations()
        self.read_reserved_dates()
        if not self._reservations:
            clear_screen()
            self._view.print_message("No hay reservas existentes")
            self._view.print_message("Presione cualquier tecla para continuar...")
            wait_key()
            return
        while True:
            clear_screen()
            self._view.print_reservations(self._reservations)
            index = self._view.request_index()
            if index.isnumeric():
                if int(index) >= 1 and int(index) <= len(self._reservations):
                    clear_screen()
                    data = self._reservations[int(index) - 1]
                    days_diference = self.calculate_diference(data[1])
                    self.delete_reservation(int(index))
                    self.delete_date(int(index))
                    if days_diference >= 15:
                        self._view.print_message(f"El reintegro es de un total de: ${float(data[2]) * 0.06}")
                    else:
                        self._view.print_message("No hay reintegro debido a que quedan menos de 15 días para la reserva.")
                    self._view.print_message("Presione cualquier tecla para continuar...")
                    wait_key()
                    break
                elif index == "0":
                    break
                else:
                    self._view.print_message("Ingrese un número válido")
                    self._view.print_message("Presione cualquier tecla para continuar...")
                    wait_key()
            else:
                self._view.print_message("Ingrese una opción válida")
                self._view.print_message("Presione cualquier tecla para continuar...")
                wait_key()

    
    def menu(self):
        #Menu
        option = ""
        while True:
            clear_screen()
            option = self._view.request_menu_option()
            match option:
                case "1":
                    self.consult_date()
                case "2":
                    self.register_reservation()
                case "3":
                    self.cancel_reservation()
                case "0":
                    clear_screen()
                    break
                case _:
                    self._view.print_message("Ingrese una opción válida")
                    self._view.print_message("Presione una tecla para continuar...")
                    wait_key()