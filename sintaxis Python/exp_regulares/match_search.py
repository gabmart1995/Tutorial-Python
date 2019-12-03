import re

nombre1 = "Lara López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "Jara López"

cadena1 = "Jara Lopez"
cadena2 = "56565647"
cadena3 = "a886876876"

codigo1 = "dufhsdihdfidufhsiufh71jfdsofjdsij"
codigo2 = "duf71sdihdfidufhsiufhjfdsofjdsij"
codigo3 = "dufhsdihdfidufhsiufhjfdsofjdsij"



# match realiza una busqueda y muestra los resultados al principio de la cadena de texto
# es sensible a mayusculas y minusculas se desabilita el CASESentive

"""if re.match( "Sandra", nombre4, re.IGNORECASE ):
	print( "Hemos encontrado el nombre" )

else:
	print( "No lo hemos encontrado" )"""

"""if re.match( ".ara", nombre1, re.IGNORECASE ):
	print( "Hemos encontrado el nombre" )

else:
	print( "No lo hemos encontrado" )"""

# \d = digito
"""if re.match( "\d", cadena2 ):
	print( "Hemos encontrado el nombre" )

else:
	print( "No lo hemos encontrado" )"""

# search busca en toda la cadena
"""if re.search( "López", nombre1  ):
	print( "Hemos encontrado el nombre" )

else:
	print( "No lo hemos encontrado" )"""

if re.search( "71", codigo2 ):
	print( "Hemos encontrado el nombre" )

else:
	print( "No lo hemos encontrado" )
