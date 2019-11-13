""" 
	Los generadores son funciones especiales que permiten 
	devolver valores una cierta cantidad de veces.
"""

def generaPares( limite ):  # return funcion tradicional
							# yield  funcion generador
	num = 1 
	# miLista = []

	while num < limite:
		
		# miLista.append( num * 2 )

		yield num * 2
		num += 1

	# return miLista


# print( generaPares( 10 ) )

devuelvePares = generaPares( 10 ) # estado de suspención

"""for i in devuelvePares:
	print( i ) """

# next: devuelve el primer valor almacenado en su interior
print( next( devuelvePares ) )

print( "Aqui podria ir mas codigo" )
print( next( devuelvePares ) )

print( "Aqui podria ir mas codigo" )
print( next( devuelvePares ) )
