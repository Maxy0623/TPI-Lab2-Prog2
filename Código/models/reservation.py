from models.client import Client

class Reservation:
    def __init__(self, client, date, services):
        self.client = client
        self.date = date
        self.services = services
        self.subtotal = 0
        self.total = 0
        self.advance_payment = 0

    #Getters
    def get_client(self):
        return self.client
    
    def get_date(self):
        return self.date
    
    def get_services(self):
        return self.services
    
    def get_subtotal(self):
        return self.subtotal
    
    def get_admin_expenses(self):
        return self.admin_expenses
    
    def get_total(self):
        return self.total
    
    def get_advance_payment(self):
        return self.advance_payment
    
    #Setters
    def set_client(self, client):
        if isinstance(client, Client):
            self.client = client
            return True
        else:
            return False
    
    def set_date(self, date):
        if type(date) == str and len(date) == 10:
            self.date = date
            return True
        else:
            return False
        
    def set_services(self, services):
        if type(services) == list and services:
            self.services = services
            return True
        else:
            return False
    
    #Otras Funciones
    #Calcular subtotal (suma de los precios individuales de cada servicio elegido).
    def _calculate_subtotal(self):
        for service in self.services:
            self.subtotal += service.get_price()
        return

    #Se calcula el total sumando gastos administrativos e IVA. Además se calcula la seña.
    def calculate_total(self):
        self._calculate_subtotal()
        admin_expenses = self.subtotal * 0.10
        iva = self.subtotal * 0.21
        self.total = self.subtotal + admin_expenses + iva
        self.advance_payment = self.total * 0.30
        return
