# Ejercicios sobre el uso del while en Python

# ejercicio 2
print( "Comparacion del metodo while \n" )

numero = int( input( "ingrese un número: " ) )
suma = 0

while numero >= 0:

	suma += numero
	numero = int( input( "ingrese un número: " ) )

print( "El resultado de la sumatoria es:", suma )