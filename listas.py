lista = [ "Maria", "Pepe", "Martha", "Antonio" ]
lista2 = [ "Maria", 5, True, 78.35 ]

print( lista ) 		# imprime la lista completa
print( lista[2] ) 	# accede a la posicion
print( lista[1:3] )	# incluye un rango y muestra el resultado
print( lista[2:] ) 	# desde hasta el final

lista.append( "Sandra" ) # agrega un elemento al final de la lista
lista.insert( 2, "Pedro" ) # agrega un elemento en una posicion en especifico

# agrega un array completo al existente
lista.extend([ "Ana", "Gabriel", "Fernando"]) 

#imprime la posicion donde se halla ana
print( lista.index( "Ana" ) ) 

# comprueba si existe si el elemento existe y devuelve un verdadero o falso
print( "Pepe" in lista )

lista.remove( "Antonio" )
print( lista )

lista.pop() # elimina el ultimo elemento de la lista
print( lista )

lista3 = lista + lista2 # une las listas en una sola
print( lista3 )