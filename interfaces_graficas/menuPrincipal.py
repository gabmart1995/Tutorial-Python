from tkinter import *
from tkinter import messagebox  # libreria de ventanas emergentes

# ventanas emergentes
def infoSoftware():
	messagebox.showinfo( "Procesador de gabriel", "Procesador de textos, version 2019" )

def avisoLicencia():
	messagebox.showwarning( "Licencia", "producto bajo licencia GNU" )

def salirAplicacion():
	
	# valor = messagebox.askquestion( "Salir", "¿Deseas salir de la aplicacion?" )
	valor = messagebox.askokcancel( "Salir", "¿Deseas salir de la aplicacion?" )

	if valor:
		root.destroy()

def cerrarDocumento():
	
	valor = messagebox.askretrycancel( "Reintentar", "No es posible cerrar documento bloqueado" )

	if valor == False:
		root.destroy()

root = Tk()
root.title( "Menu principal" )

# menu
barraMenu = Menu( root )

root.config( menu = barraMenu, width = 300, height = 300 )

# establece los items de menu
archivoMenu = Menu( barraMenu, tearoff = 0 )

# sub-menu
archivoMenu.add_command( label = "Nuevo" )
archivoMenu.add_command( label = "Abrir" )
archivoMenu.add_command( label = "Guardar" )
archivoMenu.add_command( label = "Guardar Como" )

# separador
archivoMenu.add_separator()

archivoMenu.add_command( label = "Cerrar", command = cerrarDocumento )
archivoMenu.add_command( label = "Salir", command = salirAplicacion )

# ------------------------------------- #

archivoEdicion = Menu( barraMenu, tearoff = 0 )

archivoEdicion.add_command( label = "copiar" )
archivoEdicion.add_command( label = "cortar" )
archivoEdicion.add_command( label = "pegar" )

# ---------------------------------------- #

archivoHerramientas = Menu( barraMenu, tearoff = 0 )

# ---------------------------------------- #

archivoAyuda = Menu( barraMenu, tearoff = 0 )

archivoAyuda.add_command( label = "Licencia", command = avisoLicencia )
archivoAyuda.add_command( label = "Acerca de", command = infoSoftware )

# ----------------------------------------- #

# añade el nombre del componente del menu
barraMenu.add_cascade( label = "Archivo", menu = archivoMenu )
barraMenu.add_cascade( label = "Edicion", menu = archivoEdicion )
barraMenu.add_cascade( label = "Herramientas", menu = archivoHerramientas )
barraMenu.add_cascade( label = "Ayuda", menu = archivoAyuda )

root.mainloop()