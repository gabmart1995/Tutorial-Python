import pickle

"""
Proceso de creacion del archivo binario

listaNombres = [ "Pedro", "Ana", "Maria", "Isabel" ]

# escritura binaria
ficheroBinario = open( "lista_nombres", "wb" )

# volcado
pickle.dump( listaNombres, ficheroBinario )

ficheroBinario.close()

del ( ficheroBinario )

"""

# proceso de lectura archivo binario 
fichero = open( "lista_nombres", "rb" )

listaNombres = pickle.load( fichero )

print( listaNombres )

fichero.close() 