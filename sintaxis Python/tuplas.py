tupla = ( "Juan", 30, 10, 1995 )
print( tupla[1] )

# convierte la tupla en una lista
lista = list( tupla )
print( tupla )
print( lista )

# convierte la lista en una tupla 
tupla2 = tuple( lista )
print( tupla2 )

# identifica si existe este elemento dentro de la tupla
print( "Juan" in tupla2 )

# count nos permite averiguar cuantos elementos existen dentro de tupla
print( tupla2.count( 10 ) )

# len averigua la longitud de una tupla
print( len( tupla2 ) )

#tupla unitaria RECUERDA SU SINTAXIS
tupla3 = ( "Gabriel", )
print( len( tupla3 ) )

# empaquetado y desempaquetado de tuplas
ejemploTupla = ( "Juan", 30, 10, 1995 )
nombre, dia, mes, anio = ejemploTupla

print( nombre )
print( dia )
print( mes )
print( anio )