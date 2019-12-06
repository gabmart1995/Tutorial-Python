def funcionDecoradora( funcionParametro ):

	def funcionInterior( *args, **kwargs ):

		# acciones adicionales que decoran
		print( "Vamos a realizar un calculo" )
		
		funcionParametro( *args, **kwargs ) # puede recibir una infinidad de parametros

		# acciones adicionales que decoran
		print( "hemos terminado el calculo" )

	return funcionInterior


# llama a la funcion decoradora ( acciones adicionales )

@funcionDecoradora
def suma( num1, num2, num3 ):
	print( num1 + num2 + num3 )

@funcionDecoradora
def resta( num1, num2 ):
	print( num1 - num2 )

@funcionDecoradora
def potencia( base, exponente ):
	print( pow( base, exponente ) )


suma( 7, 10, 8 )
resta( 25, 5 )

# argumentos clave valor
potencia( base = 5, exponente = 3 )

