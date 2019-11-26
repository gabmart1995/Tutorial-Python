import sqlite3

conexion = sqlite3.connect( "PrimeraBase" )

puntero = conexion.cursor()

# sql = "CREATE TABLE productos ( nombreArticulo varchar( 50 ), precio integer, seccion varchar( 20 ) );"
# sql = "INSERT INTO productos VALUES( 'balon', 15, 'deportes' )" 

# puntero.execute( sql )

"""variosProductos = [
	( "camiseta", 10, "deportes" ),
	( "jarron", 90, "ceramica" ),
	( "juguetes", 10, "jugueteria" )
]

# consulta parametrizada
sql = "INSERT INTO productos VALUES( ?, ?, ? )"

# ingresa varios registros
puntero.executemany( sql, variosProductos )"""

# consulta select
sql = "SELECT * FROM productos"

puntero.execute( sql )

variosProductos = puntero.fetchall()

# print( variosProductos ) obtiene todos los elementos de la lista

for producto in variosProductos:
	print( "Articulo:", producto[0], "\tSeccion:", producto[2], "\tPrecio", producto[1] )

# ejecuta el almacenamiento de archivos
conexion.commit()


conexion.close()