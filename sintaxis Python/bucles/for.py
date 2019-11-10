""" 
	Sintaxis for

	el elemento a recorrer puede ser una variable, tupla, 
	cadena, etc

	for variable in elemento a recorrer:
		cuerpo del bucle


for i in [1, 2, 3]:
	print( i ) # imprime 3 veces

for estaciones in ["primavera", "verano", "otono", "invierno"]:
	print( estaciones )  # imprime 4 veces

# recorriendo strings consultar la documentacion

for k in ['pildoras', 'informaticas']:

	if ( k == 'informaticas' ):
		print( k, end="\n" )
	else: 
		print( k, end=" " )


	El segundo parametro del print le dice a python que finalice la
	expresion con un salto o espacio 
"""

for i in range( 5, 10 , 2 ):
	print( "valor de la cadena: " + str( i ) ) 

	# print( f"valor de la cadena: { i }" ) 
	# la funcion f dentro de print nos perimte realizar una notacion especial y jugar con datos 
	# de diferente formato Python 3.6


valido = False
email = input( "introduce tu email: " )

# len( variable ) obtiene la logitud de la cadena
# print( len( email ) )

for i in range( len( email ) ):

	if ( email[i] == '@' ):
		valido = True


if ( valido ):
	print( "el email es correcto" )
else:
	print( "email incorrecto" ) 
