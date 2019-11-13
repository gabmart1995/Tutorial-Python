""" 
	Cuando se le agrega un asterisco 
	a un parametro de una funcion 
	quiere deceir que a recibir una cantidad 
	enorme de elementos. Y los recibe en 
	forma de tupla
"""

def devuelveCiudades( *ciudades ):

	# crea el objeto iterable
	for elemento in ciudades:

		#for subElemento in elemento:
		#	yield subElemento

		# puede ser sustituido por:
		yield from elemento

ciudadesDevueltas = devuelveCiudades( "Madrid", "Barcelona", "Caracas", "Paris" )

print( next( ciudadesDevueltas ) )
print( next( ciudadesDevueltas ) )
