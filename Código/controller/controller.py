from view.view import View
from models.date import Date
from datetime import datetime

class Controller:
    def __init__(self):
        self._today = datetime.now().date().__str__
        self._view = View()

    def is_date_reserved(self, date):
        #Abrimos el archivo en modo lectura y buscamos una coincidencia.
        with open(r"resources\reserved_dates.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line == date:
                    #Si se encuentra una coincidencia devolvemos True
                    return True
                else:
                    pass
            #Si no encontramos coincidencia en ninguna linea devolvemos False
            return False
    
    def add_date_to_file(self, date):
        with open(r"resources\reserved_dates.txt", "a") as file:
            file.write(date)

    def date_validation(self):
        while True:
            year = self._view.request_date("año" ,"YYYY")
            if len(year) == 4:
                break
            else:
                self._view.print_message("Ingrese el año en el formato solicitado")
                continue
        while True:
            month = self._view.request_date("mes", "MM")
            if int(month) <= 12 and len(month) == 2:
                break
            else:
                self._view.print_message("Ingrese un mes valido (01 ~ 12)")
                continue
        while True:
            day = self._view.request_date("dia", "DD")
            if month in ["01", "03", "05", "07", "08", "10", "12"]:
                    if int(day) <= 31:
                        break
                    else:
                        self._view.print_message(f"El mes {month} solo tiene 31 días")
            elif month in ["04", "06", "09", "11"]:
                    if int(day) <= 30:
                        break
                    else:
                        self._view.print_message(f"El mes {month} solo tiene 30 días")
            elif month == "02":
                    if int(year) % 4 == 0:
                        if int(day) <= 29:
                            break
                        else:
                            self._view.print_message(f"Febrero en el año {year} solo tiene 29 días")
                    else:
                        if int(day) <= 28:
                            break
                        else:
                            self._view.print_message(f"Febrero en el año {year} solo tiene 28 días")
        return year, month, day
    
    def menu(self):
        option = ""
        while True:
            option = self._view.request_menu_option()
            match option:
                case "1":
                    year, month, day = self.date_validation()
                    date = f"{year}/{month}/{day}"
                    if not self.is_date_reserved(date):
                        self._view.print_message("La fecha está disponible")
                    else:
                        pass
                case _:
                    break