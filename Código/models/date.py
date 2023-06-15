class Date:
    #Constructor
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        
    #Getters
    def get_year(self):
        return self._year
    
    def get_month(self):
        return self._month
    
    def get_day(self):
        return self._day
    
    #Setters
    def set_year(self, year):
        if type(year) == str and year.isnumeric() and len(year) == 4 and int(year) > 0:
            self._year = year
            return True
        else:
            return False
        
    def set_month(self, month):
        if type(month) == str and month.isnumeric() and int(month) <= 12 and int(month) >= 1:
            self._month = month
            return True
        else:
            return False
    
    #Otras funciones
    def __str__(self):
        return f"{self._year}/{self._month}/{self._day}"