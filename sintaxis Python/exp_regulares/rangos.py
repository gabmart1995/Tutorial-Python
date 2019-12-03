import re

# los rangos nos permiten buscar ciertas cantidad de caracteres

listaNombres = [ 'Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia' ]

listaCodigos = [ 'Ma.1', 'Se2', 'Ma2', 'Ba1', 'Ma:3', 'Val1', 'Val2', 'Ma4', 'MaA', 'Ma.5', 'MaB', 'Ma:C' ] 

"""for elemento in listaNombres:
 	
 	# busca entre los caracteres o hasta la t
 	# es sensible a mayusculas y minusculas 
 	if re.findall( '[o-t]', elemento ):
 		print( elemento )

 	# busca el rango al principio del elemento
 	if re.findall( '^[O-T]', elemento ):
 		print( elemento )

 	# busca al final del elemento
 	if re.findall( '[o-t]$', elemento ):
 		print( elemento )"""


for elemento in listaCodigos:
 	
 	"""if re.findall( 'Ma[0-3]', elemento ):
 		print( elemento )"""

 	# matriz de negacion
 	"""if re.findall( 'Ma[^0-3]', elemento ):
 		print( elemento )"""

 	# numeros + letras	
 	"""if re.findall( 'Ma[0-3A-B]', elemento ):
 		print( elemento )"""

 	# busqueda por caracter especial
 	if re.findall( 'Ma[.:]', elemento ):
 		print( elemento )
