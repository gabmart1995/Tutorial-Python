# Ejercicios sobre el uso del while en Python

# ejercicio 1
print( "\nComparacion del metodo while\n" )

numero = int( input( "ingrese un numero: " ) )
numeroAnterior = 0

while numero > numeroAnterior:

	numeroAnterior = numero
	numero = int( input( "ingrese un numero: " ) )

print( "\n", numero, "no es mayor que:", numeroAnterior )