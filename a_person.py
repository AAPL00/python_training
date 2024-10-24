class Person:
    
    def __init__(self, name, age, ci):  #Constructor de la clase self hace referencia a el objeto y sus parámetros
        self.name = name                #pasan a ser los atributos de la clase
        self.age =  age                 #Se me olvió validar los atributos aquí
        self.ci = ci

    def set_name(self, name):
        self.name = name
    
    def set_age(self, name):  #La forma correcta de acceder a los miembros de la clase es con la sintaxis self.atributo
        self.name = name
    
    def set_age(self, age):
        if str(type(age)) == "<class 'int'>" and age >= 0 and age <= 120:  #La función type devuelve el typo del argumento
            self.age = age                                                 #pasado con el formato <class 'tipo'> que es en si
        else:                                                              #mismo un objeto de tipo type
            return ("Not a valid age")
    
    def set_ci(self, ci):
        if len(ci) == 11:
            self.ci = ci
        else:
            return ("Not a valid ci")
    
    def show(self):
        return self.name, self.age, self.ci
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_ci(self):
        return self.ci