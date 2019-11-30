import sqlite3
from packageMessages import Messages

class DataBase():

	def __init__( self ):

		self.__sql = ""
		self.conexion = None
		self.__puntero = None
		self.data = []
		self.messages = Messages()
		
 
	def connectBD( self, method ):

		self.conexion = sqlite3.connect( "Usuarios" )

		self.puntero = self.conexion.cursor()

		if method == "createBD":

			self.__createTable()

		elif method == "create":

			self.__createUser()

		
	def __createTable( self ):

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

		try:

			self.puntero.execute( self.__sql )

			self.messages.showInfoCreateDB()

		except:

			self.messages.showInfoIsDBExists()

		finally:

			self.closeConexion()

	def __createUser( self ):
		
		# remueve el id
		self.data.remove( self.data[0] )

		self.__sql = "INSERT INTO DatosUsuarios VALUES ( NULL, ?, ?, ?, ?, ? );"

		try:
			
			self.puntero.execute( self.__sql, self.data )
			self.conexion.commit()
			
			self.messages.showInfoInsert()

		except: 

			self.messages.showWarningInsert()
			
		finally:

			self.closeConexion()


	def closeConexion( self ):

		self.puntero.close()
		self.__sql = ""

	