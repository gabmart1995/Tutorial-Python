# Ejercicios sobre el uso del while en Python

# ejercicio 2
print( "Comparacion del metodo while \n" )

numero = int( input( "ingrese un numero: " ) )
suma = 0

while numero >= 0:

	suma += numero
	numero = int( input( "ingrese un numero: " ) )

print( "El resultado de la sumatoria es:", suma )