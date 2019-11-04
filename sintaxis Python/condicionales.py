def evaluacion( nota ):

	valoracion = ""

	if nota < 5:
		valoracion = "Insufiente"

	elif nota < 6:
		valoracion = "Suficiente"

	elif nota < 7: 
		valoracion = "Bien"

	elif nota < 9: 
		valoracion = "Notable"

	else: 
		valoracion = "Sobresaliente"

	return valoracion

# ejecucion del programa en Python
print( "Programa de evaluacion de notas de alumnos" )

# pide al usuario un dato por teclado

notaAlumno = int( input( "Ingrese la nota del alumno: " )) 
print( evaluacion( notaAlumno ) )