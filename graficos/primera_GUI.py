from tkinter import *

# raiz (primera ventana)
raiz = Tk()
raiz.title( "Ventana de pruebas" )
# raiz.iconbitmap( "./../img/logo_python.gif" )

# redimensionar ancho y alto
raiz.resizable( True, True )
raiz.config( bg = "blue" )

# frame de la aplicacion
miFrame = Frame()
miFrame.pack()

miFrame.config( bg = "white" )
miFrame.config( width = "650", height = "350" )

# bordes del frame
miFrame.config( bd = 20 )
miFrame.config( relief = "ridge" )

miFrame.config( cursor = "pirate" )

raiz.mainloop()  # apertura de ventanas ( bucle infinito )

# Notas:

# se expande con el tamaño de la raiz
# miFrame.pack( fill = "both", expand = "True" )

# establece coordenadas para construir el frame
# miFrame.pack( side = "right", anchor = "s" )

# se expande de forma horizontal
# miFrame.pack( fill = "x" )

# se expande de forma vertical
# miFrame.pack( fill = "y", expand = "True" )