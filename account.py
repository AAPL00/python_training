#La implementación es ridícula porque el ejercicio lo es
class Account:

    def __init__(self, owner, cuantity = 0): #Con la sintaxis parameter = "value" se asigna un valor por defecto para el
        self.owner = owner                   #parámetro en caso de que a la función no se le envíe un argumento
        self.cuantity = cuantity

    def set_owner(self, owner):
        return "NOP"
    
    def set_cuantity(self, cuantity):
        return "NOP"
    
    def get_owner(self):
        return self.owner
    
    def get_cuantity(self):
        return self.cuantity
    
    def show(self):
        return (self.owner, self.cuantity)
    
    def add_cuantity(self, cuantity):
        if cuantity > 0:
            self.cuantity += cuantity
        else:
            return "What are you trying to do?"
        
    def retire_cuantity(self, cuantity):
        self.cuantity -= cuantity

class YoungAccount(Account):

    def __init__(self, owner, cuantity=0, bonification = 0):  
        super().__init__(owner, cuantity)  #El método super() (no es un método exactamente sino una funcion que devuelve un
        self.bonification = bonification   #objeto de proxy que permite acceder a los métodos de la clase padre) permite
                                           #aprovechar la funcionalidad de la clase padre sin  una instancia separada
    def set_bonification(self, bonification):
        self.bonification = bonification

    def get_bonification(self):
        return self.bonification
    
    def is_valid_owner(self, age):
        valid
        if int(age) >= 18 and int(age) < 25:
            valid = True
        else:
            valid = False
    
    def retire_cuantity(self, cuantity, age):
        if self.is_valid_owner(age):
            return super().retire_cuantity(cuantity)
        else:
            return "Not a valid user"
        
    def show(self):
        return ("Young account", self.bonification)