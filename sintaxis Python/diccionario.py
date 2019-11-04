diccionario = {
	"Alemania" : "Berlin",
	"Francia" : "Paris",
	"Reino Unido" : "Londres",
	"Espana" : "Madrid",
	"Venezuela" : "Caracas" 
}

# imprime el diccionario
print( diccionario )
print( diccionario["Venezuela"] )

# agregar un elemento al diccionario
diccionario[ "Italia" ] = "Roma"
diccionario[ "Grecia" ] = "Atenas"

"""
	Python puede sobreescrbir valores
	erroneos simplemente aplicando la
	misma sintaxis
"""

# eliminar un elemento del diccionario
del diccionario["Reino Unido"]
print( diccionario )

# diccionario combinado
diccionario2 = {
	"Alemania" : "Berlin",
	23 : "Jordan",
	"Mosqueteros" : 3
}

print( diccionario2 )

# combinacion de diccionario + tupla
tupla = ( "Espana", "Francia", "Reino Unido", "Alemania" )

diccionario3 = {
	tupla[0] : "Madrid",
	tupla[1] : "Paris",
	tupla[2] : "Londres",
	tupla[3] : "Berlin" 	
}

print( diccionario3 )
print( diccionario3[ tupla[3] ] )
print( diccionario[ "Francia" ] )

# formas de diccionario
deportista = {
	23 : "Jordan",
	"nombre" : "Michael",
	"equipo" : "Chicago",
	"anillos" : [ 1991, 1992, 1993, 1996, 1997, 1998 ], # lista
	"temporadas" : {  # diccionario
		"anio": [ 1991, 1992, 1993, 1996, 1997, 1998 ]
	}
}

print( deportista )
print( deportista["equipo"] )

# accede a un elemento especifico dentro de la clave
print( deportista["anillos"][1] ) 
print( deportista["temporadas"]["anio"][3] )

# muestra las claves de los diccionarios
print( diccionario.keys() )
print( diccionario2.keys() )
print( diccionario3.keys() )
print( deportista.keys() )

# muestra los valores
print( diccionario.values() )
print( diccionario2.values() )
print( diccionario3.values() )
print( deportista.values() )

# imprime la longitud del diccionario
print( len( diccionario ) )
print( len( diccionario2 ) )
print( len( diccionario3 ) )
print( len( deportista ) )