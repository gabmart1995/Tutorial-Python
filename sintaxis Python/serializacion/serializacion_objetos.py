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
	

coche1 = Vehiculo( "Mazda", "MX5" )
coche2 = Vehiculo( "Seat", "Leon" )
coche3 = Vehiculo( "Renault", "Megane" )

coches = [ coche1, coche2, coche3 ]

# serializacion
fichero = open( 'coches', "wb" )
pickle.dump( coches, fichero )
fichero.close()

del( fichero )

