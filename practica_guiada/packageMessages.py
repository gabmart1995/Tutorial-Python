from tkinter import messagebox

class Messages():
	
	def showInfoCreateDB( self ):

		messagebox.showinfo( "BBDD", "Base de datos, creada con exito" )

	def showInfoIsDBExists( self ):

		messagebox.showwarning( "¡Atención!", "La base de datos ya existe" )

	def getInfoClose( self ):

		valor = messagebox.askquestion( "Salir", "¿Deseas salir de la aplicación?")
		return valor