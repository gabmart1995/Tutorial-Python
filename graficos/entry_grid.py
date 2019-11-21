from tkinter import *

root = Tk()

root.title( "Entry and Grid" )

frame = Frame( root, width = 600, height = 300 )
frame.pack()

# grid(): construye una tabla con filas y columnas
# row : fila
# column : columna 


nombreLabel = Label( frame, text = "Nombre:" )
nombreLabel.grid( row = 0, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroNombre = Entry( frame )
cuadroNombre.grid( row = 0, column = 1, padx = 10, pady = 10 )
# cuadroNombre.config( fg = "blue", justify = "center" )

apellidoLabel = Label( frame, text = "Apellido:" )
apellidoLabel.grid( row = 2, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroApellido = Entry( frame )
cuadroApellido.grid( row = 2, column = 1, padx = 10, pady = 10 )

direccionLabel = Label( frame, text = "Dirección:" )
direccionLabel.grid( row = 3, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroDireccion = Entry( frame )
cuadroDireccion.grid( row = 3, column = 1, padx = 10, pady = 10 )

passLabel = Label( frame, text = "Contrasena:" )
passLabel.grid( row = 1, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroPass = Entry( frame )
cuadroPass.grid( row = 1, column = 1, padx = 10, pady = 10 )
cuadroPass.config( show = "*" )  # password


root.mainloop() 