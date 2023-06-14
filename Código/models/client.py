class Client:
    #Constructor
    def __init__(self, name, dni):
        self._name = name
        self._dni = dni

    #Getters
    def get_name(self):
        return self._name
    
    def get_dni(self):
        return self._dni
    
    #Setters
    #Se retorna un booleano para usar desde el controller llamando a la vista para imprimir un mensaje
    def set_name(self, name):
        if type(name) == str:
            self._name = name
            return True
        else:
            return False 

    def set_dni(self, dni):
        if type(dni) == str and dni.isnumeric() and len(dni) == 8:
            self._dni = dni
            return True
        else:
            return False

    #Otras Funciones   
    def __str__(self):
        return f"{self.get_name()} - {self.get_dni()}"