"""numeroPar = lambda num: num % 2 == 0
numeros = [ 17, 24, 7, 39, 8, 51, 92 ]

print( list( filter( numeroPar, numeros ) ) )"""

class Empleado():
	
	def __init__( self, nombre, cargo, salario ):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	def __str__( self ):
		return "{} que trabaja como {} tiene un salario de {} $".format( self.nombre, self.cargo, self.salario )


listaEmpleados = [
	Empleado( "Juan", "Director", 75000 ),
	Empleado( "Ana", "Presidenta", 55000 ),
	Empleado( "Antonio", "Administrativo", 25000 ),
	Empleado( "Sara", "Secretaria", 27000 ),
	Empleado( "Mario", "Botones", 21000 ),
]

# filter ejecuta una condicion
salarioAlto = filter( lambda empleado: empleado.salario >= 55000, listaEmpleados )

for empleadoSalario in salarioAlto:
	print( empleadoSalario )		
