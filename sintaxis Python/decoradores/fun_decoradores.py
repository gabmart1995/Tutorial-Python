def funcionDecoradora( funcionParametro ):

	def funcionInterior():

		# acciones adicionales que decoran
		print( "Vamos a realizar un calculo" )
		
		funcionParametro()

		# acciones adicionales que decoran
		print( "hemos terminado el calculo" )

	return funcionInterior


# llama a la funcion decoradora ( acciones adicionales )

@funcionDecoradora
def suma():
	print( 15 + 20 )

@funcionDecoradora
def resta():
	print( 30 - 10 )


suma()
resta()
