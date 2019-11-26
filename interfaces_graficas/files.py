from tkinter import *
from tkinter import filedialog

def abrirArchivo():

	# obtiene la ruta donde se almacena el archivo
	fichero = filedialog.askopenfilename( 
		title = "Abrir", 
		initialdir = "/home/gabriel/", 

		# filtros de archivos tupla
		filetypes = ( 
			( "Archivos de word 95-03", "*.doc" ),
			( "Archivo de texto", "*.txt" ), 
			( "Todos los  archivos", "*.*" )
		) 
	)

	print( fichero )

root = Tk()
root.title( "Manipulacion de archivos" )

Button( root, text = "Abrir archivo", command = abrirArchivo ).pack()

root.mainloop()