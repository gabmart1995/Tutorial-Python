from tkinter import messagebox

class Messages():

	""" clase destinada para los mensajes al usuario  """
	
	def showInfoCreateDB( self ):
		return messagebox.showinfo( "BBDD", "Base de datos, creada con exito" )

	def showInfoIsDBExists( self ):
		return messagebox.showwarning( "¡Atención!", "La base de datos ya existe" )

	def getInfoClose( self ):

		valor = messagebox.askquestion( "Salir", "¿Deseas salir de la aplicación?" )
		return valor

	def showInfoInsert( self ):
		return messagebox.showinfo( "BBDD", "Registro insertado con éxito" )

	def showWarningInsert( self ):
		return messagebox.showwarning( "¡Atención!", "Error al insertar usuario" )

	def showWarningID( self ):
		return messagebox.showwarning( "¡Atención!", "El usuario con ese id no existe" )

	def showInfoUpdate( self ):
		return messagebox.showinfo( "BBDD", "Registro actualizado con éxito" )

	def showWarningUpdate( self ):
		return messagebox.showwarning( "¡Atención!", "Error al actualizar usuario" )

	def showInfoDelete( self ):
		return messagebox.showinfo( "BBDD", "Registro eliminado con éxito" )

	def showWarningDelete( self ):
		return messagebox.showwarning( "¡Atención!", "Error al eliminar usuario" )

	def infoSoftware( self ):
		return messagebox.showinfo( "Aplicación CRUD", "Prototipo de pruebas de CRUD,\ncreador: Gabriel Martínez,\nversion 2019" )

	def avisoLicencia( self ):
		return messagebox.showwarning( "Licencia", "Producto bajo licencia GNU" )

