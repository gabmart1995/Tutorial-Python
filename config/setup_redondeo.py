""" 
	RECUERDA descargar el paquete python3-pip
	apt-get install python3-pip
"""

from setuptools import setup

setup( 

	name = "paquete_calculos",
	version = "1.0",
	description = "Paquete de redondeo y potencia",
	author = "Gabriel Martinez",
	author_email = "gabmart1995@gmail.com",
	url = "https://gabmart1995@github.com",
	packages = [ "calculos", "calculos.operaciones_basicas", "calculos.redondeo_potencia" ]

 )