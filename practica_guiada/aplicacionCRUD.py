from tkinter import *
from packageBD import DataBase 
from packageMessages import Messages

class AppComponent():

	def __init__( self ):

		self.root = Tk()
		self.root.title( "Aplicacion CRUD" )

		self.operations = Operations()

		self.__createMenu()
		self.__createForm()
		self.__createLabels()
		self.__createButtons()


	def __setVariables( self ):

		idUser = StringVar()
		name = StringVar()
		lastName = StringVar()
		password = StringVar()
		direction = StringVar()

		self.operations.textEntry.extend([ idUser, name, lastName, password, direction ])


	def __createMenu( self ):
		
		barraMenu = Menu( self.root )
		
		# config
		self.root["menu"] = barraMenu
		self.root["width"] = 300
		self.root["height"] = 300

		bdMenu = Menu( barraMenu, tearoff = 0 )
		bdMenu.add_command( label = "Conectar", command = self.operations.dataBase.connectBD )
		bdMenu.add_separator()
		bdMenu.add_command( label = "Salir", command = self.__closeApp )

		borrarMenu = Menu( barraMenu, tearoff = 0 )
		borrarMenu.add_command( label = "Borrar campos", command = self.operations.clear )

		crudMenu = Menu( barraMenu, tearoff = 0 )
		crudMenu.add_command( label = "Crear" )
		crudMenu.add_command( label = "Leer" )
		crudMenu.add_command( label = "Actualizar" )
		crudMenu.add_command( label = "Borrar" )

		ayudaMenu = Menu( barraMenu, tearoff = 0 )
		ayudaMenu.add_command( label = "Licencia" )
		ayudaMenu.add_command( label = "Acerca de ..." )

		# cascade
		barraMenu.add_cascade( label = "BBDD", menu = bdMenu )
		barraMenu.add_cascade( label = "Borrar", menu = borrarMenu )
		barraMenu.add_cascade( label = "CRUD", menu = crudMenu )
		barraMenu.add_cascade( label = "Ayuda", menu = ayudaMenu )

	def __createForm( self ): 

		self.frameForm = Frame( self.root )
		self.frameForm.pack()

		self.__setVariables()

		textId = Entry( self.frameForm, textvariable = self.operations.textEntry[0] )
		textId.grid( row = 0, column = 1, padx = 10, pady = 10 )

		textName = Entry( self.frameForm, textvariable = self.operations.textEntry[1] )
		textName.grid( row = 1, column = 1, padx = 10, pady = 10 )

		textPassword = Entry( self.frameForm, textvariable = self.operations.textEntry[2] )
		textPassword.grid( row = 2, column = 1, padx = 10, pady = 10 )
		textPassword.config( show = "*" )

		textLastName = Entry( self.frameForm, textvariable = self.operations.textEntry[3] )
		textLastName.grid( row = 3, column = 1, padx = 10, pady = 10 )
	
		textDirection = Entry( self.frameForm, textvariable =  self.operations.textEntry[4] )
		textDirection.grid( row = 4, column = 1, padx = 10, pady = 10 )

		textArea = Text( self.frameForm, width = 16, height = 5 )
		textArea.grid( row = 5, column = 1, padx = 10, pady = 10 )

		scrollVert = Scrollbar( self.frameForm, command = textArea.yview )
		scrollVert.grid( row = 5, column = 2, sticky = "nsew" )

		textArea.config( yscrollcommand = scrollVert.set )

		self.operations.textArea = textArea
	

	def __createLabels( self ):

		idLabel = Label( self.frameForm, text = "Id:" )
		idLabel.grid( row = 0, column = 0, sticky = "e", padx = 10, pady = 10 )

		nameLabel = Label( self.frameForm, text = "Nombre:" )
		nameLabel.grid( row = 1, column = 0, sticky = "e", padx = 10, pady = 10 )

		passLabel = Label( self.frameForm, text = "Contraseña:" )
		passLabel.grid( row = 2, column = 0, sticky = "e", padx = 10, pady = 10 )

		lastNameLabel = Label( self.frameForm, text = "Apellido:" )
		lastNameLabel.grid( row = 3, column = 0, sticky = "e", padx = 10, pady = 10 )

		directionLabel = Label( self.frameForm, text = "Dirección:" )
		directionLabel.grid( row = 4, column = 0, sticky = "e", padx = 10, pady = 10 )

		comentaryLabel = Label( self.frameForm, text = "Comentarios:" )
		comentaryLabel.grid( row = 5, column = 0, sticky = "e", padx = 10, pady = 10 )


	def __createButtons( self ):

		self.frameButtons = Frame( self.root )
		self.frameButtons.pack()

		createButton = Button( self.frameButtons, text = "Crear" )
		createButton.grid( row = 0, column = 0, sticky = "e", padx = 10, pady = 10 )

		readButton = Button( self.frameButtons, text = "Leer" )
		readButton.grid( row = 0, column = 1, sticky = "e", padx = 10, pady = 10 )

		updateButton = Button( self.frameButtons, text = "Actualizar" )
		updateButton.grid( row = 0, column = 2, sticky = "e", padx = 10, pady = 10 )

		deleteButton = Button( self.frameButtons, text = "Borrar" )
		deleteButton.grid( row = 0, column = 3, sticky = "e", padx = 10, pady = 10 )


	def __closeApp( self ):

		opcion = self.operations.messages.getInfoClose()

		if opcion == "yes":
			self.root.destroy()


	def loop( self ):
		self.root.mainloop()


class Operations():

	def __init__( self ):

		self.textArea = None

		self.textEntry = []

		self.dataBase = DataBase()
		self.messages = Messages()

	def clear( self ):

		for entry in self.textEntry:
			
			entry.set( "" )

		self.textArea.delete( 1.0, END )	


# ----------------------------------------------------------- #

app = AppComponent()
app.loop()