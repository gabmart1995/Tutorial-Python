from io import open

""" 
	Modos de apertura de archivos

	lectura = r
	escritura = w
	append = a  ( permite agregar informacion en un archivo que ya existe )
"""


# Metodo de Escritura

archivo_texto = open( "archivo.txt", "w" )

frase = "Estupendo dia para estudiar Python"
archivo_texto.write( frase )

archivo_texto.close()  # cierra  el archivo en memoria

"""
	Esta forma permite leer el archivo y su informacion almacenarla 
	en una variable
"""

"""
	Manipula el archivo existente

archivo_texto = open( "archivo.txt", "a" )
archivo_texto.write( "\nsiempre es una buena ocasion para estudiar Python" )
archivo_texto.close()

"""
"""

Metodo solo lectura.
archivo_texto = open( "archivo.txt", "r" )  

# convierte la informacion en una lista manipulable
# lineas_texto = archivo_texto.readline() 
# archivo_texto.close()

# print( lineas_texto[0] )

# seek permite posicionar la posicion del cursor en una posicion especifica

# lee la mitad de la informacion
archivo_texto.seek( len( archivo_texto.read() ) / 2 )
print( archivo_texto.read() )

archivo_texto.seek( len( archivo_texto.readline() ) )
print( archivo_texto.read() )

# lee el contenido del archivo y lo almacena en la variable texto

# seek permite ubicar la posicion de un cursor en una posicion especifica
archivo_texto.seek( 11 ) 

texto = archivo_texto.read( 11 )
print( texto )

print( archivo_texto.read() )

archivo_texto.close()

"""
"""
# lectura y escritura
archivo_texto = open( "archivo.txt", "r+" ) 

# archivo_texto.write( "Comienzo del texto" )
# print( archivo_texto.readlines() )

lista_texto = archivo_texto.readlines()
lista_texto[ 0 ] = "Esta linea ha sido incluida desde el exterior\n"

archivo_texto.seek( 0 )

archivo_texto.writelines( lista_texto ) 

archivo_texto.close()

"""