# programa que pide los datos personales del usuario

print( "\nDatos personales\n" )

nombre = raw_input( "Ingrese su nombre: " )
direccion = raw_input( "Ingrese la direccion: "  )
telefono = raw_input( "Ingrese su telefono: " )

datosPersonales = [ nombre, direccion, telefono ]

print( "\nnombre: " + datosPersonales[0] + "\ndireccion: " 
	 + datosPersonales[1] + "\ntelefono: " + datosPersonales[2]
	 + "\n")