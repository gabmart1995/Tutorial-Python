"""def areaTriangulo( base, altura ):
	return ( base * altura ) / 2

# lambda permite simplificar datos de este estilo

print( areaTriangulo( 5, 7 ) ) """

"""# sintaxis lambda
# areaTriangulo = lambda base, altura: ( base * altura ) / 2

print( areaTriangulo( 7,5 ) )
print( areaTriangulo( 9, 6 ) )

cubo = lambda num: pow( num, 3 ) 
# cubo = lambda num: num ** 3

print( cubo( 13 ) )"""

destacarValor = lambda comision: "¡{}! $".format( comision )
comisionAna = 15585

print( destacarValor( comisionAna ) )