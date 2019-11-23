from tkinter import *

root = Tk()
root.title( "Radio button" )

opcion = IntVar()  

def imprimir():
	
	if opcion.get() == 1:

		etiqueta.config( text = "has elegido masculino" )

	else:

		etiqueta.config( text = "has elegido femenino" )

	# print( "el valor seleccionado es:", opcion.get() )


Label( root, text = "Género" ).pack()

Radiobutton( 
	root, 
	text = "masculino", 
	variable = opcion, 
	value = 1, 
	command = imprimir 
).pack()

Radiobutton( 
	root, 
	text = "femenino", 
	variable = opcion, 
	value = 2, 
	command = imprimir
).pack()

etiqueta = Label( root )
etiqueta.pack()

root.mainloop()