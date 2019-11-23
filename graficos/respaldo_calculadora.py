from tkinter import *

# --------- Calculadora app ---------------------- #

# frame
app = Tk()

app.title( "Calculadora Python" )

frame = Frame( app )
frame.pack()

# ------------- variables globales ----------- #

operacion = ""
resetPantalla = True
resultado = 0

# -------------- Pantalla ------------------ #

numeroPantalla = StringVar()
numeroPantalla.set( "0" )

pantalla = Entry( frame, textvariable = numeroPantalla )
pantalla.grid( row = 1, column = 1, padx = 10, pady = 10, columnspan = 5 )
pantalla.config( background = "black", fg = "#03f943", justify = "right" )

# columnspan toma 4 posiciones de la grilla

# --------- Pulsaciones Teclado --------------#

def numeroPulsado( num ):
	
	global operacion
	global resetPantalla

	if resetPantalla:

		numeroPantalla.set( num )
		resetPantalla = False

	else:

		numeroPantalla.set( numeroPantalla.get() + num )


def suma( num ): 	# suma
	
	global operacion
	global resultado
	global resetPantalla

	resultado += int( num )

	operacion = "suma"

	resetPantalla = True 

	numeroPantalla.set( resultado )

def resta( num ):  # resta

	global operacion
	global resultado
	global resetPantalla

	if resultado == 0:

		resultado = int( num )

	else:

		resultado -= int( num )

		numeroPantalla.set( resultado )

	operacion = "resta"
	resetPantalla = True

def multi( num ):

	global operacion
	global resultado
	global resetPantalla

	if resultado == 0:

		resultado = int( num )

	else:

		resultado *= int( num )

		numeroPantalla.set( resultado )

	operacion = "multi"
	resetPantalla = True

def division( num ):

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


	operacion = "division"
	resetPantalla = True

def el_resultado():  # boton igual
	
	global resultado
	global operacion

	if operacion == "suma":
		
		numeroPantalla.set( resultado + int( numeroPantalla.get() ) )

	elif operacion == "resta":
		
		numeroPantalla.set( resultado - int( numeroPantalla.get() ) )

	elif operacion == "multi":
		 
		 numeroPantalla.set( resultado * int( numeroPantalla.get() ) )

	elif operacion == "division":

		try:

			numeroPantalla.set( resultado / float( numeroPantalla.get() ) )

		except ZeroDivisionError:

			numeroPantalla.set( "error de sintaxis" )

	resultado = 0
	operacion = ""


def clear( nameMethod ):  # clear y allclear

	global operacion
	global resetPantalla
	global resultado

	if nameMethod == "allclear":   # limpia toda la operacion

		numeroPantalla.set( "0" )

		operacion = ""
		resetPantalla = True
		resultado = 0

	else:
		return

# -------------- Fila 1 --------------------- #

boton7 = Button( frame, text = "7", width = 3, command = lambda:numeroPulsado( "7" ) )
boton7.grid( row = 2, column = 1 )

boton8 = Button( frame, text = "8", width = 3,  command = lambda:numeroPulsado( "8" ) )
boton8.grid( row = 2, column = 2 )

boton9 = Button( frame, text = "9", width = 3,  command = lambda:numeroPulsado( "9" ) )
boton9.grid( row = 2, column = 3 )

botonDiv = Button( frame, text = "/", width = 3, command = lambda:division( numeroPantalla.get() ) )
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

# loop infinito
app.mainloop()