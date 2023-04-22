#ESTE ES EL CONSTRUCTOR...
class Matematica:
    def suma(self):
        self.n1 = 4 #ESTAS SON VARIABLES
        self.n2 = 6

#ESTE SERIA EL OBJETO...
suma = Matematica()

suma.suma()#aqui llamamos al metodo, que primero se llama al OBJETO QUE ES SUMA y despues al metodo...
print('La suma seria ',suma.n1+suma.n2)