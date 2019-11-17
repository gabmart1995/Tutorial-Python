"""import funciones_matematicas  # importar modulos

uso de los metodos incluidos dentro de modulos 
funciones_matematicas.sumar( 7, 5 ) """

# importacion de metodos especificos  (LAZY LOAD)
# from funciones_matematicas import sumar

# importacion de todos los metodos
from funciones_matematicas import *

sumar( 7, 5 )
restar( 9, 5 )
multiplicar( 5, 6 )