import math

def raizCuadrada( listaNumeros ):

	""" 
		Funcion que devuelve una lista de una raiz cuadrada 
		pasado por el parametro

		>>> lista = []
		>>> for i in [4, 9, 16]:
		...		lista.append( i )
		>>> raizCuadrada( lista )
		[2.0, 3.0, 4.0]

		>>> lista = []
		>>> for i in [-4, 9, 16 ]:
		...		lista.append(i)
		>>> raizCuadrada( lista )
		Traceback (most recent call last):
   		...
		ValueError: math domain error
	"""

	return [ math.sqrt( num ) for num in listaNumeros ]

# print( raizCuadrada( [ 9, -16, 25, 36 ] ) )

import doctest
doctest.testmod()