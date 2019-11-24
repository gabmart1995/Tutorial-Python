from tkinter import *

def escribir():
	miNombre.set( "Gabriel" )

root = Tk()

root.title( "Entry and Grid" )

frame = Frame( root, width = 600, height = 300 )
frame.pack()

# declara una cadena para asociarla al cuadro
miNombre = StringVar()

# nombre
nombreLabel = Label( frame, text = "Nombre:" )
nombreLabel.grid( row = 0, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroNombre = Entry( frame, textvariable = miNombre )
cuadroNombre.grid( row = 0, column = 1, padx = 10, pady = 10 )

# apellido
apellidoLabel = Label( frame, text = "Apellido:" )
apellidoLabel.grid( row = 2, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroApellido = Entry( frame )
cuadroApellido.grid( row = 2, column = 1, padx = 10, pady = 10 )

# direccion
direccionLabel = Label( frame, text = "Dirección:" )
direccionLabel.grid( row = 3, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroDireccion = Entry( frame )
cuadroDireccion.grid( row = 3, column = 1, padx = 10, pady = 10 )

# password
passLabel = Label( frame, text = "Contraseña:" )
passLabel.grid( row = 1, column = 0, sticky = "e", padx = 10, pady = 10 )

cuadroPass = Entry( frame )
cuadroPass.grid( row = 1, column = 1, padx = 10, pady = 10 )
cuadroPass.config( show = "*" )  # password

# comentarios
comenLabel = Label( frame, text = "Comentarios:" )
comenLabel.grid( row = 4, column = 0, sticky = "e", padx = 10, pady = 10 )

# text
textComentario = Text( frame, width = 20, height = 5 )
textComentario.grid( row = 4, column = 1,  padx = 10, pady = 10 ) 

# scroll vertical
scrollVert = Scrollbar( frame, command = textComentario.yview )
scrollVert.grid( row = 4, column = 2, sticky = "nsew" )

# button
botonEnvio = Button( root, text = "Escribir", command = escribir )
botonEnvio.pack()

# asignacion vertical al text
textComentario.config( yscrollcommand = scrollVert.set )

root.mainloop() 