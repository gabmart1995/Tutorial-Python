class Persona():

	def __init__( self, nombre, edad, lugarResidencia ):

		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion( self ):

		print("Nombre:", self.nombre, "edad:", self.edad, "residencia:", self.lugarResidencia)

class Empleado( Persona ):

	def __init__( self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado ):

		# instruccion super llama al constructor
		super().__init__( nombre_empleado, edad_empleado, residencia_empleado )

		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion( self ):

		super().descripcion()

		print( "Salario:", self.salario, "Antiguedad:", self.antiguedad )

empleado1 = Persona( "Manuel", 55, "Venezuela" )
empleado1.descripcion()

# esta funcion identifica si un elemento pertenece a un elemento.
print( isinstance( empleado1, Persona ) )
print( isinstance( empleado1, Empleado ) )
