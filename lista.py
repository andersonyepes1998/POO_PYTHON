global list

list = list()

class Carrera:
    nombre = ""
    escuderia =""
    motor = ""
    piloto =""
    costoAnual =""

def menu():
    op = 0

    while op != 0:
        print ("Menu")
        print ('1.- Digite el Nombre')
        print ('2.- Digite la escuderia')
        print ('3.- Digite el Motor')
        print ('4.- Digite que piloto correra')
        print ('5.- Digite el costo anual de la carrera')
        print ('6.- salir')
        op = input ('Digite la opcion: ')

