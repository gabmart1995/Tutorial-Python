# Programa que valida un cadena de texto

# print( correo.find('@') )  = devuelve 0 en la primera posicion
# print( correo.endswith( '@' ) ) =  devuelve verdadero si el parametro esta bicado de ultimo
# print( correo.rfind( '@' ) ) = devuelve la ultima posicion del elemento
# print( correo.find('@') ) =  inicia desde el principio de la cadena
# print( len( correo ) ) =
# print( len( correo ) - 1 ) devuelve la longitud de la cadena

correo = input( "Ingresa tu correo: " )

if correo.count('@') != 1 or correo.find('@') == 0 or correo.endswith('@'):
	print( "Correo incorrecto" )

else:
	print( "correo correcto" )

"""
Solucion 2

if correo.count('@') != 1 or ( correo.find( '@' ) == len( correo ) -1 ) or ( correo.find( '@' ) == 0 ):
	print( "Correo incorrecto" )

else:
	print( "correo correcto" )"""


"""
Solucion 3
	
if ( correo.count('@') != 1 or correo.rfind( '@' ) ) == ( len( correo ) - 1 ) or correo.find( '@' ) == 0 :
	
	print( "Correo incorrecto" )

else: 
	print( "Correo correcto" ) """


