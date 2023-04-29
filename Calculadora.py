#class Ropa:
#    def __init__(self):
#        self.marca = 'YODAIS'
#        self.talla = 'M'
#        self.color = 'RED'

#camisa = Ropa()
#print(camisa.talla)
#print(camisa.marca)
#print(camisa.marca)

class Calculadora:
    def __init__(self):
        self.__suma = None
        self.__resta = None
        self.__multiplicacion = None
        self.__divicion = None

    @property
    def suma(self):
        return self.__suma
    
    @property
    def resta(self):
        return self.__resta
    
    @property
    def multiplicacion(self):
        return self.__multiplicacion
    
    @property
    def divicion(self):
        return self.__divicion
    
    #SET

    @suma.setter
    def suma (self,dato):
        self.__suma=dato

    @resta.setter
    def resta (self,dato):
        self.__resta=dato
    
    @multiplicacion.setter
    def multiplicacion (self,dato):
        self.__multiplicacion=dato
    
    @divicion.setter
    def divicion (self,dato):
        self.__divicion=dato

    def operaciones():
        print('calculo')