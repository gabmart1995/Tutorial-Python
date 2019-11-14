# ejemplo de uso correcto de try - except

def divide():

	try: 

		op1 = float( input("Introduce el primer numero: ") )
		op2 = float( input("Introduce el segundo numero: ") )

		print( "La division es:" + str( op1 / op2 ) )
	
	except ValueError:
		
		print( "El valor introducido es erroneo" )

	except ZeroDivisionError:

		print( "No se puede dividir entre 0" )

	finally:
		
		print( "Calculo finalizado" )

divide()