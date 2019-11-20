# ejemplo de como crear un archivo permanente

import pickle

class Persona():

	def __init__( self, nombre, genero, edad ):

		self.nombre = nombre
		self.genero = genero
		self.edad = edad

		print( "Se ha creado una persona nueva con el nombre de", self.nombre )
	
	def __str__( self ):

		# investigar
		return "{} {} {}".format( self.nombre, self.genero, self.edad )


class ListaPersonas():

	personas = []

	def __init__( self ):

		listaDePersonas = open( "ficheroExterno", "ab+" )
		listaDePersonas.seek( 0 )

		try:

			self.personas = pickle.load( listaDePersonas )

			print( "Se cargaron {} personas del fichero externo".format( len( self.personas ) ) )

		except:

			print( "El fichero esta vacio" )

		finally:

			listaDePersonas.close()

			del( listaDePersonas ) # borra en memoria la lista de personas

	def agregarPersonas( self, persona ):

		# agrega a la persona a la lista
		self.personas.append( persona )
		self.guardarPersonasFicheroExterno()

	def mostrarPersonas( self ):

		for p in self.personas:
			print( p )

	def guardarPersonasFicheroExterno( self ):

		listaDePersonas = open( "ficheroExterno", "wb" )

		pickle.dump( self.personas, listaDePersonas )
		
		listaDePersonas.close()
		
		del( listaDePersonas )

	def mostrarInfoFicheroExterno( self ):

		print( "La informacion del fichero externo es la siguiente" )

		self.mostrarPersonas()


miLista = ListaPersonas()

persona1 = Persona( "Ana", "Femenino", 19 )

miLista.agregarPersonas( persona1 )
miLista.mostrarInfoFicheroExterno()
