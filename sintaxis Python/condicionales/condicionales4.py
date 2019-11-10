print( "\nPrograma de becas anio 2019\n" )

distanciaEscuela = int( input( "introduce la distancia a la escuela en km: " ) )
numeroHermanos = int( input( "introduce el numero de hermanos en el centro: " ) )
salarioFamiliar = int( input( "introduce el salario anual bruto: " ) )

# utltiza comparacion de and y or para unir o separar comparaciones

if distanciaEscuela > 40 and numeroHermanos > 2 and salarioFamiliar <= 20000:
	print( "\nTienes derecho a una beca\n" )

else:
	print( "\nNo tienes derecho a beca\n" ) 

# ===========================================================================

print( "Asignturas optativas 2017\n" )
print( "Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad\n" )

opcion = raw_input( "Escribe la asignatura escogida: " )

asignatura = opcion.lower() 	# transforma la opcion en munisculas

if asignatura in ( "informatica grafica", "pruebas de software", "usabilidad y accesibilidad" ):
	print( "Asignatura elegida: " + asignatura + "\n" )

else: 
	print( "La asignatura no esta contemplada\n" )