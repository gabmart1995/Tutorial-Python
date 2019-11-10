# programa que valida un email en Python 
def validarCorreo( miCorreo ):

	valorContador = 0

	for palabra in miCorreo:

		if ( palabra == '.' or palabra == '@' ):
			valorContador += 1

	return valorContador


miCorreo = input( "Ingrese tu correo: " )
contador = validarCorreo( miCorreo )


if ( contador == 2 ):
	print( "El email es correcto" )
else:
	print( "El email no es correcto" )