import re  # importa la libreria expresiones regulares

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis secilla"

textoBuscar = "Python"

textoEncontrado = re.search( textoBuscar, cadena )

# indica la posicion donde inicia y donde termina
print( textoEncontrado.start() )
print( textoEncontrado.end() )
print( textoEncontrado.span() )

print( len ( re.findall( textoBuscar, cadena ) ) )

# search busca el texto dentro de la cadena
"""if re.search( textBuscar, cadena ) != None:
	print( "He encontrado el texto" )

else:
	print( "No he encontrado el texto" )"""
