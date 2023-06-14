class Service:
    #Constructor
    def __init__(self, service, price):
        self._service = service
        self._price = price

    #Getters
    def get_service(self):
        return self._service
    
    def get_price(self):
        return self._price
    
    #Setters
    def set_service(self, service):
        if type(service) == str:
            self._service = service
            return True
        else:
            return False
        
    def set_price(self, price):
        if type(price) == str and price.isnumeric() and int(price) > 0:
            self._price
            return True
        else:
            return False