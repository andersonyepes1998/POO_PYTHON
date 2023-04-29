from Calculadora import Calculadora

n1 = int(input('Primer numero: '))
n2 = int(input('Segundo numero: '))

objeto = Calculadora()
objeto.suma = n1 + n2
objeto.resta = n1 - n2
objeto.multiplicacion = n1 * n2
objeto.divicion = n1/n2

print('La suma es igual a: ',objeto.suma)
print('La resta es igual a: ',objeto.resta)
print('La multiplicacion es igual a: ',objeto.multiplicacion)
print('La divicion es igual a: ',objeto.divicion)