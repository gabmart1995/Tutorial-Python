import pickle

class Vehiculo():
	
	def __init__( self, marca, modelo ):
		
		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.accelera = False
		self.frena = False

	def arrancar( self ):
		
		self.enMarcha = True

	def accelerar( self ):
		
		self.accelera = True

	def frenar( self ):
		
		self.frena = True

	def estado( self ):
		
		print( "Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha,
			"\nAccelerando:", self.accelera, "\nFrenando:", self.frena )



# lectura del archivos
ficheroApertura = open( "coches", "rb" )
misCoches = pickle.load( ficheroApertura )

ficheroApertura.close()

for c in misCoches:
	print( c.estado() )