class Areas():

	""" Esta clase calcula el area de diferentes figuras geometricas  """
	
	def areaCuadrado( lado ):
	
		""" calcula el area de un cuadrado """
		return "el área del cuadrado es: " + str( lado * lado )

	def areaTriangulo( base, altura ):

		"""  calcula el area de un triangulo """
		return "el área del triangulo es: " + str( ( base * altura ) / 2 )		



# imprime los comentarios asociados a la función 
# print( areaCuadrado.__doc__ )

# documentacion de metodos
# help( areaCuadrado ) 
# help( areaTriangulo )

# documentacion de clases
help( Areas )


# print( areaTriangulo( 2, 7 ) )