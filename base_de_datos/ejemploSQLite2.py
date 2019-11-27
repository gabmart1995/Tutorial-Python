import sqlite3

conexion = sqlite3.connect( "GestionProductos" )

puntero = conexion.cursor()

# las triples comillas permiten construir senctencias de asignaciones largas
"""create = ''' 
	CREATE TABLE productos (
		id integer PRIMARY KEY AUTOINCREMENT,
		nombreArticulo varchar( 50 ) UNIQUE,
		precio integer,
		seccion varchar( 20 )
	);
'''

productos = [ 

	( "pelota", 20, "jugueteria" ),
	( "pantalon", 15, "confeccion" ),
	( "destornillador", 25, "ferreteria" ),
	( "jarron", 45, "ceramica" ),
]

# insertar datos con campos autoincrementales
insert = "INSERT INTO productos VALUES ( null, ?, ?, ? );"

puntero.execute( create ) 
puntero.executemany( insert, productos ) """


# CRUD 

# READ
select = "SELECT * FROM productos WHERE seccion = 'confeccion'"
puntero.execute( select )

productos = puntero.fetchall()

print( productos )

# UPDATE
"""update = "UPDATE productos SET precio = 35 WHERE nombreArticulo = 'pelota' "
puntero.execute( update )"""

# DELETE
"""delete = "DELETE FROM productos WHERE id = 5"
puntero.execute( delete ) """

conexion.commit()

conexion.close()