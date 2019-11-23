import tkinter as tk

class Application( tk.Frame ):

	boton = None  # None = null
	salir = None

	# constructor
	def __init__( self, master = None ):

		tk.Frame.__init__( self, master )
		self.pack()

		self.crearComponentes()

	def crearComponentes( self ):

		# se monta una estructura de la aplicacion

		self.boton = tk.Button( self )
		self.boton[ "text" ] = "Hola mundo\n(Click me)"
		self.boton[ "command" ] = self.mensaje

		self.boton.pack( side = "top" )

		self.salir = tk.Button( self )
		self.salir[ "text" ] = "salir"
		self.salir[ "command" ] = root.destroy
		self.salir.config( fg = "red" )

		self.salir.pack( side = "bottom" )

	def mensaje( self ):
		print( "Hola que tal a todos" )


root = tk.Tk()
root.title( "Hola mundo" )

app = Application( master = root )
app.mainloop()
