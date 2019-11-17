# nombreUsuario = input( "Introduce un nombre: " )
edad = input( "Introduce la edad: " )

# print( "el nombre es:", nombreUsuario.upper()  )
# print( "el nombre es:", nombreUsuario.lower()  )
# print( "el nombre es:", nombreUsuario.capitalize()  )


while edad.isdigit() == False: # True o False

	print( "Coloca un valor numerico" )
	edad = input( "Introduce la edad: " )


if int( edad ) < 18:
	print( "No puede pasar" ) 

else:
	print( "Puedes pasar" )