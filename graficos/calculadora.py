from tkinter import *

# frame
root = Tk()

root.title( "Calculadora Python" )

frame = Frame( root )
frame.pack()

# -------------- Pantalla ------------------ #

numeroPantalla = StringVar()

pantalla = Entry( frame, textvariable = numeroPantalla )
pantalla.grid( row = 1, column = 1, padx = 10, pady = 10, columnspan = 4 )
pantalla.config( background = "black", fg = "#03f943", justify = "right" )

# columnspan toma 4 posiciones de la grilla

# --------- Pulsaciones Teclado --------------#

def numeroPulsado( numero ):
	numeroPantalla.set( numeroPantalla.get() + numero )


# -------------- Fila 1 --------------------- #

boton7 = Button( frame, text = "7", width = 3, command = lambda:numeroPulsado( "7" ) )
boton7.grid( row = 2, column = 1 )

boton8 = Button( frame, text = "8", width = 3,  command = lambda:numeroPulsado( "8" ) )
boton8.grid( row = 2, column = 2 )

boton9 = Button( frame, text = "9", width = 3,  command = lambda:numeroPulsado( "9" ) )
boton9.grid( row = 2, column = 3 )

botonDiv = Button( frame, text = "/", width = 3 )
botonDiv.grid( row = 2, column = 4 )

# -------------- Fila 2 --------------------- #

boton4 = Button( frame, text = "4", width = 3, command = lambda:numeroPulsado( "4" ) )
boton4.grid( row = 3, column = 1 )

boton5 = Button( frame, text = "5", width = 3, command = lambda:numeroPulsado( "5" ) )
boton5.grid( row = 3, column = 2 )

boton6 = Button( frame, text = "6", width = 3, command = lambda:numeroPulsado( "6" ) )
boton6.grid( row = 3, column = 3 )

botonMulti = Button( frame, text = "x", width = 3 )
botonMulti.grid( row = 3, column = 4 )

# -------------- Fila 3 --------------------- #

boton1 = Button( frame, text = "1", width = 3, command = lambda:numeroPulsado( "1" ) )
boton1.grid( row = 4, column = 1 )

boton2 = Button( frame, text = "2", width = 3, command = lambda:numeroPulsado( "2" ) )
boton2.grid( row = 4, column = 2 )

boton3 = Button( frame, text = "3", width = 3, command = lambda:numeroPulsado( "3" ) )
boton3.grid( row = 4, column = 3 )

botonRest = Button( frame, text = "-", width = 3 )
botonRest.grid( row = 4, column = 4 )

# -------------- Fila 4 --------------------- #

boton0 = Button( frame, text = "0", width = 3, command = lambda:numeroPulsado( "0" ) )
boton0.grid( row = 5, column = 1 )

botonComa = Button( frame, text = ",", width = 3, command = lambda:numeroPulsado( "," ) )
botonComa.grid( row = 5, column = 2 )

botonIgual = Button( frame, text = "=", width = 3 )
botonIgual.grid( row = 5, column = 3 )

botonSuma = Button( frame, text = "+", width = 3 )
botonSuma.grid( row = 5, column = 4 )


root.mainloop()