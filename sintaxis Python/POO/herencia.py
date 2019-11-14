class Vehiculo():  # SuperClase

	# constructor
	# self corresponde al objeto propio de la clase
	
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


class Furgoneta( Vehiculo ): # herencia
	
	def cargar( self, carga ):
		
		self.cargado = carga

		if self.cargado:
			return "La furgoneta esta cargada"

		else:
			return "La furgoneta no esta cargada"


class Moto( Vehiculo ):  # herencia
	
	hCaballito = ""

	def caballito( self ):
		self.hCaballito = "voy haciendo el caballito"

	# sobreescritura de funciones
	def estado( self ):

		print( "Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha,
			"\nAccelerando:", self.accelera, "\nFrenando:", self.frena, "\n" + self.hCaballito, "\n" )


class VElectricos():

	def __init__( self ):
		self.autonomia = 100

	def cargarBaterias( self ):
		self.cargando = True


class BicicletaElectica( Vehiculo, VElectricos ): # herencia multiple
	pass


miMoto = Moto( "Honda", "CBR" )
miMoto.caballito() # ejecuta el caballito
miMoto.estado()

miFurgoneta = Furgoneta( "Renault", "Kangoo" )
miFurgoneta.arrancar()
miFurgoneta.estado()
print( miFurgoneta.cargar( True ), "\n" )

miBici = BicicletaElectica( "Orbea", "HT1030" ) # declaracion de un objeto
miBici.estado()