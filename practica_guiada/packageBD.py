import sqlite3
from packageMessages import Messages

class DataBase():

	""" clase destinada a realizar las consultas hacia la BD """

	def __init__( self ):

		self.__sql = ""
		self.conexion = None
		self.__puntero = None
		self.data = []  	
		self.records = []
		self.messages = Messages()
		
 
	def connectBD( self, method ):

		""" funcion que inicia la conexion con la BD  """

		self.conexion = sqlite3.connect( "Usuarios" )
		self.puntero = self.conexion.cursor()

		if method == "createBD":
			self.__createTable()

		elif method == "create":
			self.__createUser()

		elif method == "read":
			self.__readUser()

		elif method == "update":
			self.__updateUser()

		else:
			self.__deleteUser()

	def __createTable( self ):

		""" crea las tablas de la BD  """

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

			self.__closeConexion()

	def __createUser( self ):

		""" crea un registro de usuario  """
		
		self.data.remove( self.data[0] )

		self.__sql = "INSERT INTO DatosUsuarios VALUES ( NULL, ?, ?, ?, ?, ? );"

		try:
			
			self.puntero.execute( self.__sql, self.data )
			self.conexion.commit()

			self.messages.showInfoInsert()

		except: 

			self.messages.showWarningInsert()
			
		finally:

			self.__closeConexion()


	def __updateUser( self ):

		""" actualiza un usuario  """

		datosUsuarios = self.data[1], self.data[2], self.data[3], self.data[4], self.data[5]
		idUser = self.data[0]

		self.__sql = "UPDATE DatosUsuarios SET nombreUsuario = ?, password = ?, apellido = ?, direccion = ?,comentario = ? WHERE id = "
		self.__sql += idUser + ";"

		try:

			self.puntero.execute( self.__sql, datosUsuarios )
			self.conexion.commit()
			self.messages.showInfoUpdate()

		except:
			self.messages.showWarningUpdate()
			
		finally:
			self.__closeConexion()


	def __readUser( self ):

		""" consulta un usuario """

		idUser = self.data[0]

		self.__sql = "SELECT * FROM DatosUsuarios WHERE id =" + idUser


		self.puntero.execute( self.__sql )
		self.records = self.puntero.fetchall()

		if self.records == []:
			self.messages.showWarningID()

		self.conexion.commit()
	
		self.__closeConexion()

	def  __deleteUser( self ):

		""" elimina un usuario """

		idUser = self.data[0]

		self.__sql = "DELETE FROM DatosUsuarios WHERE id =" + idUser

		try:
			
			self.puntero.execute( self.__sql )
			self.conexion.commit()
			self.messages.showInfoDelete()

		except:
			self.messages.showWarningDelete()

		finally: 
			self.__closeConexion()

	def __closeConexion( self ):

		""" funcion que cierra la conexion  """

		self.puntero.close()
		self.__sql = ""
		self.data = []