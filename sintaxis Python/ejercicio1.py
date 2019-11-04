# programa que calcula el mayor de 2 numeros por teclado
def devuelveMax( num1, num2 ):

	# devuelve el mensaje en string
	if ( num1 > num2 ):
		return "el numero mayor es: " +  str( num1 )

	elif ( num1 < num2 ): 
		return "el numero mayor es: " + str( num2 )

	else: 
		return "Son iguales"

print( "\nPrograma que devuelve el mayor de 2 numeros\n" )

num1 = int( input( "ingrese el primer valor: " ) )
num2 = int( input( "ingrese el segundo valor: " ) )

print( "\n" + devuelveMax( num1, num2 ) + "\n" ) 