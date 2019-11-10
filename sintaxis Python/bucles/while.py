# ciclo while

i = 1

while i <= 10:
	print( "Ejecución " + str( i ) )
	i += 1

print( "termino la ejecución" )

edad = int( input( "ingresa tu edad: " ) )

while edad < 5 or edad > 100:
	
	print( "ingresa tu edad correcta. Vuelve a intentarlo" )
	edad = int( input( "ingresa tu edad: " ) )

print( "Gracias por colaborar" )
print( "Edad del aspirante: " + str( edad ) + "\n" )

import math  # importa la clase math de Python

print( "Programa de calculo de raiz cuadrada" )

numero = int( input( "introduce un número: " ) )
intentos = 0	

while numero < 0:

	print( "No se puede hallar la raiz de un numero negativo" )

	if intentos == 2:

		print( "Has consumido bastantes intentos el programa ha finalizado" )
		break

	numero = int( input( "introduce un número: " ) )

	if numero < 0:
		intentos += 1

if intentos < 2:

	solucion = math.sqrt( numero ) 
	print( "La raiz cuadrada de " + str( numero ) + " es: " + str( solucion ) )