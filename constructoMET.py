class Ropa:
    def __init__(self):
        self.marca = 'YODAIS'
        self.talla = 'M'
        self.color = 'RED'

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)


class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1*n2
        self.divicion = n1 / n2

operacion = Calculadora(4,6)
print(operacion.suma)
print(operacion.multiplicacion)
print(operacion.divicion)