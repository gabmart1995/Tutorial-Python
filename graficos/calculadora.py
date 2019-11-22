from tkinter import *

# --------- Pulsaciones Teclado --------------#

def numeroPulsado( numero ):
	
	global variableTemporal
	global operacionAlmacenada

	cerosIzquierda()	

	if variableTemporal != '':  # chequea la operacion

		numeroPantalla.set( numero )
		operacionAlmacenada = variableTemporal

		variableTemporal = ''

	else:

		numeroPantalla.set( numeroPantalla.get() + numero )


def cerosIzquierda():  # evalua los ceros a la izquierda

	if numeroPantalla.get() == "0":

		numeroPantalla.set( "" )

	else: 

		return

# ----------------------------------------------#

def suma( num ): 	# suma
	
	global variableTemporal
	global resultado

	resultado += int( num )

	variableTemporal = "suma" 

	# aparece el resultado en pantalla
	numeroPantalla.set( resultado )

def multi( num ):	# multiplicacion
	pass

def resta( num ):
	pass

def division( num ):
	pass

# ------------- El resultado ------------------ #

def el_resultado():
	
	global resultado
	global operacionAlmacenada

	if operacionAlmacenada == "suma":
		
		numeroPantalla.set( resultado + int( numeroPantalla.get() ) )

	elif operacionAlmacenada == "resta":
		
		numeroPantalla.set( resultado - int( numeroPantalla.get() ) )

	elif operacionAlmacenada == "multi":
		 
		 numeroPantalla.set( resultado * int( numeroPantalla.get() ) )

	elif operacionAlmacenada == "division":

		numeroPantalla.set( resultado / int( numeroPantalla.get() ) )

	# vacia las variables
	operacionAlmacenada = ""
	resultado = 0


# ----------------- Clear ---------------------#

def clear( method ):

	global resultado
	global operacionAlmacenada
	global variableTemporal 

	if method == 'allclear':

		operacionAlmacenada = ""
		variableTemporal = ""

		resultado = 0

		numeroPantalla.set( "0" )


# --------- Calculadora ---------------------- #

# frame
root = Tk()

root.title( "Calculadora Python" )

frame = Frame( root )
frame.pack()

# variables globales
variableTemporal = ""
operacionAlmacenada = ""

resultado = 0

# -------------- Pantalla ------------------ #

numeroPantalla = StringVar()
numeroPantalla.set( "0" )

pantalla = Entry( frame, textvariable = numeroPantalla )
pantalla.grid( row = 1, column = 1, padx = 10, pady = 10, columnspan = 5 )
pantalla.config( background = "black", fg = "#03f943", justify = "right" )

# columnspan toma 4 posiciones de la grilla

# -------------- Fila 1 --------------------- #

boton7 = Button( frame, text = "7", width = 3, command = lambda:numeroPulsado( "7" ) )
boton7.grid( row = 2, column = 1 )

boton8 = Button( frame, text = "8", width = 3,  command = lambda:numeroPulsado( "8" ) )
boton8.grid( row = 2, column = 2 )

boton9 = Button( frame, text = "9", width = 3,  command = lambda:numeroPulsado( "9" ) )
boton9.grid( row = 2, column = 3 )

botonDiv = Button( frame, text = "/", width = 3 )
botonDiv.grid( row = 2, column = 4 )

botonAllClear = Button( 
	frame, 
	text = "AC", 
	width = 3, 
	height = 3, 
	command = lambda:clear( 'allclear' )  
)

botonAllClear.grid( row = 2, column = 5, rowspan = 2 )


# -------------- Fila 2 --------------------- #

boton4 = Button( frame, text = "4", width = 3, command = lambda:numeroPulsado( "4" ) )
boton4.grid( row = 3, column = 1 )

boton5 = Button( frame, text = "5", width = 3, command = lambda:numeroPulsado( "5" ) )
boton5.grid( row = 3, column = 2 )

boton6 = Button( frame, text = "6", width = 3, command = lambda:numeroPulsado( "6" ) )
boton6.grid( row = 3, column = 3 )

botonMulti = Button( frame, text = "x", width = 3, command = lambda:multi( numeroPantalla.get() ))
botonMulti.grid( row = 3, column = 4 )

# -------------- Fila 3 --------------------- #

boton1 = Button( frame, text = "1", width = 3, command = lambda:numeroPulsado( "1" ) )
boton1.grid( row = 4, column = 1 )

boton2 = Button( frame, text = "2", width = 3, command = lambda:numeroPulsado( "2" ) )
boton2.grid( row = 4, column = 2 )

boton3 = Button( frame, text = "3", width = 3, command = lambda:numeroPulsado( "3" ) )
boton3.grid( row = 4, column = 3 )

botonRest = Button( frame, text = "-", width = 3, command = lambda:resta( numeroPantalla.get() ) )
botonRest.grid( row = 4, column = 4 )

botonAllClear = Button( 
	frame, 
	text = "C", 
	width = 3, 
	height = 3, 
	command = lambda:clear()  
)

botonAllClear.grid( row = 4, column = 5, rowspan = 2 )

# -------------- Fila 4 --------------------- #

boton0 = Button( frame, text = "0", width = 3, command = lambda:numeroPulsado( "0" ) )
boton0.grid( row = 5, column = 1 )

botonComa = Button( frame, text = ",", width = 3, command = lambda:numeroPulsado( "," ) )
botonComa.grid( row = 5, column = 2 )

botonIgual = Button( frame, text = "=", width = 3, command = lambda:el_resultado() )
botonIgual.grid( row = 5, column = 3 )

botonSuma = Button( frame, text = "+", width = 3, command = lambda:suma( numeroPantalla.get() ) )
botonSuma.grid( row = 5, column = 4 )


root.mainloop()