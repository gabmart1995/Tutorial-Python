import sqlite3
from packageMessages import Messages

class DataBase():

	def __init__( self ):

		self.__sql = ""
		self.__puntero = None
		self.messages = Messages()


	def connectBD( self ):

		conexion = sqlite3.connect( "Usuarios" )

		self.puntero = conexion.cursor()

		try:

			self.createTable()
			self.messages.showInfoCreateDB()

		except:

			self.messages.showInfoIsDBExists()

		finally:

			self.closeConexion()


	def createTable( self ):

		self.__sql = '''

			CREATE TABLE DatosUsuarios (
				id integer PRIMARY KEY AUTOINCREMENT,
				nombreUsuario varchar( 50 ),
				password varchar( 50 ),
				apellido varchar( 50 ),
				direccion varchar( 50 ),
				comentario varchar( 100 ) 
			);
		'''

		self.puntero.execute( self.__sql )


	def closeConexion( self ):

		self.puntero.close()