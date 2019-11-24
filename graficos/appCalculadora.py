import tkinter as tk

class AppCalculadora( tk.Frame ):


	def __init__( self, master  ):

		tk.Frame.__init__( self, master )
		self.pack()

		# clase operaciones
		self.operaciones = Operaciones()

		self.crearComponentes()

	def capturarNumero( self, num ):
		
		global operacion
		global resetPantalla

		if resetPantalla:

			numeroPantalla.set( num )
			resetPantalla = False

		else: 

			numeroPantalla.set( numeroPantalla.get() + num )


	def crearComponentes( self ):  # componentes graficos

		global numeroPantalla 

		# pantalla
		self.pantalla = tk.Entry( self )
		self.pantalla["textvariable"] = numeroPantalla
		self.pantalla.grid( row = 1, column = 1, padx = 10, pady = 10, columnspan = 5  )
		self.pantalla.config(  background = "black", fg = "#03f943", justify = "right" )

		# fila 1

		# boton 7
		self.boton7 = tk.Button( self )
		self.boton7["text"] = "7"
		self.boton7["width"] = 3
		self.boton7["command"] = lambda: self.capturarNumero( "7" )

		self.boton7.grid( row = 2, column = 1 )

		# boton 8
		self.boton8 = tk.Button( self )
		self.boton8["text"] = "8"
		self.boton8["width"] = 3
		self.boton8["command"] = lambda: self.capturarNumero( "8" )

		self.boton8.grid( row = 2, column = 2 )

		# boton 9
		self.boton9 = tk.Button( self )
		self.boton9["text"] = "9"
		self.boton9["width"] = 3
		self.boton9["command"] = lambda: self.capturarNumero( "9" )

		self.boton9.grid( row = 2, column = 3 )

		# boton div
		self.botonDiv = tk.Button( self )
		self.botonDiv["text"] = "/"
		self.botonDiv["width"] = 3
		self.botonDiv["command"] = lambda: self.operaciones.div( numeroPantalla.get() )

		self.botonDiv.grid( row = 2, column = 4 )

		# boton all clear
		self.botonAllClear = tk.Button( self )
		self.botonAllClear["text"] = "AC"
		self.botonAllClear["width"] = 3
		self.botonAllClear["height"] = 3
		self.botonAllClear["command"] = lambda: self.operaciones.allClear( 'allClear' )

		self.botonAllClear.grid( row = 2, column = 5, rowspan = 2 )

		# fila 2

		# boton 4
		self.boton4 = tk.Button( self )
		self.boton4["text"] = "4"
		self.boton4["width"] = 3
		self.boton4["command"] = lambda: self.capturarNumero( "4" )

		self.boton4.grid( row = 3, column = 1 )

		# boton 5
		self.boton5 = tk.Button( self )
		self.boton5["text"] = "5"
		self.boton5["width"] = 3
		self.boton5["command"] = lambda: self.capturarNumero( "5" )

		self.boton5.grid( row = 3, column = 2 )

		# boton 6
		self.boton6 = tk.Button( self )
		self.boton6["text"] = "6"
		self.boton6["width"] = 3
		self.boton6["command"] = lambda: self.capturarNumero( "6" )

		self.boton6.grid( row = 3, column = 3 )

		# boton multiplicar
		self.botonMulti = tk.Button( self )
		self.botonMulti["text"] = "x"
		self.botonMulti["width"] = 3
		self.botonMulti["command"] = lambda: self.operaciones.multi( numeroPantalla.get() )
		self.botonMulti.grid( row = 3, column = 4 )

		# fila 3

		# boton 1
		self.boton1 = tk.Button( self )
		self.boton1["text"] = "1"
		self.boton1["width"] = 3
		self.boton1["command"] = lambda: self.capturarNumero( "1" )

		self.boton1.grid( row = 4, column = 1 )

		# boton 2
		self.boton2 = tk.Button( self )
		self.boton2["text"] = "2"
		self.boton2["width"] = 3
		self.boton2["command"] = lambda: self.capturarNumero( "2" )

		self.boton2.grid( row = 4, column = 2 )

		# boton 3
		self.boton3 = tk.Button( self )
		self.boton3["text"] = "3"
		self.boton3["width"] = 3
		self.boton3["command"] = lambda: self.capturarNumero( "3" )

		self.boton3.grid( row = 4, column = 3 )

		# boton resta
		self.botonResta = tk.Button( self )
		self.botonResta["text"] = "-"
		self.botonResta["width"] = 3
		self.botonResta["command"] = lambda: self.operaciones.resta( numeroPantalla.get() )

		self.botonResta.grid( row = 4, column = 4 )

		# boton clear
		self.botonClear = tk.Button( self )
		self.botonClear["text"] = "C"
		self.botonClear["width"] = 3
		self.botonClear["height"] = 3
		self.botonClear["command"] = lambda: self.operaciones.allClear( 'clear' )

		self.botonClear.grid( row = 4, column = 5, rowspan = 2 )

		# fila 4

		# boton 0
		self.boton0 = tk.Button( self )
		self.boton0["text"] = "0"
		self.boton0["width"] = 3
		self.boton0["command"] = lambda: self.capturarNumero( "0" )

		self.boton0.grid( row = 5, column = 1 )

		# boton decimal
		self.botonDecimal = tk.Button( self )
		self.botonDecimal["text"] = "."
		self.botonDecimal["width"] = 3
		self.botonDecimal["command"] = lambda: self.capturarNumero( "." )

		self.botonDecimal.grid( row = 5, column = 2 )

		# boton igual
		self.botonIgual = tk.Button( self )
		self.botonIgual["text"] = "="
		self.botonIgual["width"] = 3
		self.botonIgual["command"] = lambda: self.operaciones.resolucion()

		self.botonIgual.grid( row = 5, column = 3 )

		# boton suma
		self.botonSuma = tk.Button( self )
		self.botonSuma["text"] = "+"
		self.botonSuma["width"] = 3
		self.botonSuma["command"] = lambda: self.operaciones.suma( numeroPantalla.get() )

		self.botonSuma.grid( row = 5, column = 4 )


# ----------------------------------------------------------------------------------------#

class Operaciones():

	def suma( self, num ):    # suma

		global operacion
		global resultado
		global resetPantalla

		if self.__isDecimal( num ) == "entero":
			resultado += int( num )

			
		elif self.__isDecimal( num ) == "decimal":
			resultado += float( num )

		else:
			return
		
		operacion = "suma"
		resetPantalla = True 
		numeroPantalla.set( resultado )
		

	def resta( self, num ):	# resta

		global operacion
		global resultado
		global resetPantalla
		
		if self.__isDecimal( num ) == "entero":
			
			if resultado == 0:
				resultado = int( num )

			else:
				resultado -= int( num )

			numeroPantalla.set( resultado )
			
		elif self.__isDecimal( num ) == "decimal":

			if resultado == 0:
				resultado = float( num )

			else:
				resultado -= float( num )

			numeroPantalla.set( resultado )
			
		else:
			return

		operacion = "resta"
		resetPantalla = True


	def multi( self, num ):	# multiplicacion
		
		global operacion
		global resultado
		global resetPantalla

		if self.__isDecimal( num ) == "decimal":

			if resultado == 0:
				resultado = float( num )

			else:
				resultado *= float( num )
				numeroPantalla.set( resultado )

		elif self.__isDecimal( num ) == "entero":

			if resultado == 0:
				resultado = int( num )

			else:
				resultado *= int( num )
				numeroPantalla.set( resultado )

		operacion = "multi"
		resetPantalla = True


	def div( self, num ):	# division
		
		global operacion
		global resultado
		global resetPantalla

		if resultado == 0:

			resultado = float( num )

		else:

			try: 

				resultado /= float( num )
				numeroPantalla.set( resultado )

			except ZeroDivisionError:

				numeroPantalla.set( "error de sintaxis" )
				resetPantalla = True

		operacion = "division"
		resetPantalla = True


	def allClear( self, method ):
		
		global operacion
		global resultado
		global resetPantalla

		if method == 'allClear':

			numeroPantalla.set( "0" )

			operacion = ""
			resultado = 0
			resetPantalla = True

		else:
			
			cadenaNumero = numeroPantalla.get()
			nuevaCadena = ""
			limite = len( cadenaNumero  ) - 1

			if cadenaNumero != "0":

				for digito in range( limite ):
					nuevaCadena += cadenaNumero[ digito ]
				
				if nuevaCadena != "":
					numeroPantalla.set( nuevaCadena )
			
				else:
					numeroPantalla.set( "0" )
					resetPantalla = True
			
			else:
				return

	def resolucion( self ):

		global resultado
		global operacion
		global resetPantalla

		if operacion == "suma":

			if self.__isDecimal( numeroPantalla.get() ) == "decimal":
				numeroPantalla.set( float( resultado ) + float( numeroPantalla.get() ) )
			
			elif self.__isDecimal( numeroPantalla.get() ) == "entero":
				numeroPantalla.set( int( resultado ) + int( numeroPantalla.get() ) )

			else:
				return
			
		elif operacion == "resta":

			if self.__isDecimal( numeroPantalla.get() ) == "decimal":
				numeroPantalla.set( float( resultado ) - float( numeroPantalla.get() ) )
			
			elif self.__isDecimal( numeroPantalla.get() ) == "entero":
				numeroPantalla.set( int( resultado ) - int( numeroPantalla.get() ) )

			else:
				return

		elif operacion == "multi":

			if self.__isDecimal( numeroPantalla.get() ) == "decimal":
				numeroPantalla.set( float( resultado ) * float( numeroPantalla.get() ) )
			
			elif self.__isDecimal( numeroPantalla.get() ) == "entero":
				numeroPantalla.set( int( resultado ) * int( numeroPantalla.get() ) )

			else:
				return
		 

		elif operacion == "division":

			try:
				numeroPantalla.set( float( resultado ) / float( numeroPantalla.get() ) )

			except ZeroDivisionError:

				numeroPantalla.set( "error de sintaxis" )
				resetPantalla = True


		resultado = 0
		operacion = ""

	
	# funcion de identificacion de decimales
	def __isDecimal( self, num ):
		
		global resetPantalla

		if num.count('.') >= 2 or num.find('.') == 0 or num.endswith('.'):
			
			numeroPantalla.set( "error de sintaxis" )
			resetPantalla = True
		
		elif num.count( '.' ) == 1:

			return "decimal"
				
		else:

			return "entero"

# ---------------------------------------------------------------------------- #

root = tk.Tk()
root.title( "Calculadora" )

# variables globales
numeroPantalla = tk.StringVar()
numeroPantalla.set( "0" )

operacion = ""

resultado = 0

resetPantalla = True

# inicio de la aplicacion
app = AppCalculadora( master = root )

app.mainloop()		
