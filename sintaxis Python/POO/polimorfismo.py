class Coche():

	def desplazamiento( self ):
		print("me desplazo utilizando 4 ruedas")

class Moto():
	
	def desplazamiento( self ):
		print("me desplazo utilizando 2 ruedas")
		
class Camion():

	def desplazamiento( self ):
		print("me desplazo utilizando 6 ruedas")
		

# desarrollo del polimorfismo
def desplazamiento( vehiculo ):
	vehiculo.desplazamiento()


miVehiculo = Coche()
desplazamiento( miVehiculo )