import re 

listaNombres = [ 'Ana Gómez', 'Maria Martin', 'Sandra López', 'Santiago Martin', 'Sandra Fernández' ]

listasIP = [ 
	'http://pildorasinformaticas.es',
	'ftp://pildorasinformaticas.es',
	'http://pildorasinformaticas.com',
	'ftp://pildorasinformaticas.es',
	'http://informaticaenespaña.es',
]

listaSustantivos = [ 'hombres', 'mujeres', 'niños', 'niñas', 'mascotas', 'camión', 'camion' ]



"""for elemento in listaNombres

	# inicia por: ^
		if re.findall( '^Sandra', elemento ):
		print( elemento )

	# finaliza por: $
		if re.findall( "Martin$", elemento ):
		print( elemento ) """

"""for elemento in listasIP:
	
	if re.findall( 'es$', elemento ):
		print( elemento )

	if re.findall( '^ftp', elemento ):
		print( elemento )

	# busca por patron de busqueda
	if re.findall( '[ñ]', elemento ):
		print( elemento ) """

for elemento in listaSustantivos:

	""" patron de busqueda
	if re.findall( 'niñ[oa]s', elemento ):
		print( elemento )"""

	if re.findall( 'cami[oó]n', elemento ):
		print( elemento )


