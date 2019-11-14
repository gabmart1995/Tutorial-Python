# mensajes de excepcion personalidas
"""
def evaluarEdad( edad ):

	if edad < 0:
		raise ValueError( "No se permiten edades negativas" )

	if edad < 20:
		return "eres muy joven"

	elif edad < 40:
		return "eres joven" 

	elif edad < 65:
		return "es maduro"

	elif edad < 100:
		return "cuidate ..."

print( evaluarEdad( 15 ) )
"""

import math

def calcularRaiz( num1 ):

	if num1 < 0:
		raise ValueError( "El numero no puede ser negativo" )

	else:
		return math.sqrt( num1 )


op1 = int( input( "introduce un numero: " ) )

try:
	print( calcularRaiz( op1 ) )

# se puede renombrar el error.
except ValueError as ErrorNumeronegativo:

	print( ErrorNumeronegativo )

print( "Programa finalizado" )