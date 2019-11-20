from tkinter import *

root = Tk()
root.title( "Práctica label" )

frame = Frame( root, width = 500, height = 400 )
frame.pack()

Label( 
	frame, 
	text = "Hola alumnos de Python", 
	fg = "red",
	font = ( "Liberation Sans", 14 )  ).place( x = 20, y = 20 )


# funciona con png y gif y se añade el parametro en la ruta
miImage = PhotoImage( file = "./../img/Firma Gabriel.png" )
Label( frame, image = miImage ).place( x = 100, y = 60 )

# miLabel = Label( frame, text = "Hola alumnos de Python" )

# este metodo permite ubicar cualquier elemento dentro de la interfaz
# miLabel.place( x = 100, y = 100 )


root.mainloop()