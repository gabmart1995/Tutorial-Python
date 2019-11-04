def verificarEdad( edadUsuario ):

	if edadUsuario < 18:
		print( "No puede ver el contenido" )

	elif edadUsuario > 100:
		print( "Edad incorrecta" )

	else:
		print( "Puedes pasar" )

# verificacion de acceso
print( "verificacion de acceso" )
edad = int( input( "introduce tu edad: " ) )

verificarEdad( edad )
print( "El programa ha finalizado" )