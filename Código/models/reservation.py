from client import Client
from date import Date

class Reservation:
    def __init__(self, client, date, services):
        self._client = client
        self._date = date
        self._services = services
        self._subtotal = None
        self._admin_expenses = None
        self._total = None
        self._advance_payment = None

    #Getters
    def get_client(self):
        return self._client
    
    def get_date(self):
        return self._date
    
    def get_services(self):
        return self._services
    
    def get_subtotal(self):
        return self._subtotal
    
    def get_admin_expenses(self):
        return self._admin_expenses
    
    def get_total(self):
        return self._total
    
    def get_advance_payment(self):
        return self._advance_payment
    
    #Setters
    def set_client(self, client):
        if isinstance(client, Client):
            self._client = client
            return True
        else:
            return False
    
    def set_date(self, date):
        if isinstance(date, Date):
            self._date = date
            return True
        else:
            return False
        
    def set_services(self, services):
        if type(services) == list and services:
            self._services = services
            return True
        else:
            return False
        
    def set_subtotal(self):
        self._subtotal = 0
        for service in self._services:
            self._subtotal += service.get_price()

    def set_admin_expenses(self):
        self._admin_expenses = self._subtotal * 0.10

    def set_total(self):
        iva = self._subtotal * 0,21
        self._total = self._subtotal + self._admin_expenses + iva

    def set_advance_payment(self):
        self._advance_payment = self._total * 0.30