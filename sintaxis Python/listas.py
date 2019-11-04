lista = [ "Maria", "Pepe", "Martha", "Antonio" ]
lista2 = [ "Maria", 5, True, 78.35 ]

print( lista ) 		# lista completa		
print( lista[2] ) 	# posicion
print( lista[1:3] )	# rango
print( lista[2:] ) 	

lista.append( "Sandra" )  	# coloca ultima posicion
lista.insert( 2, "Pedro" ) 	# coloca posicion especifica

# anade nuevos elementos a la lista
lista.extend([ "Ana", "Gabriel", "Fernando"]) 

print( lista.index( "Ana" ) )  	# obtiene el indice

# comprueba si existe si el elemento existe y devuelve un verdadero o falso
print( "Pepe" in lista )

lista.remove( "Antonio" ) 	# remueve un elemento
print( lista )

lista.pop()		# retira el ultimo elemento de la lista
print( lista )

lista3 = lista + lista2   	# combina 2 listas en una nueva
print( lista3 )