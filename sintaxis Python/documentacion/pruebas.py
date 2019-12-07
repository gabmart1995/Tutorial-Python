def compruebaEmail( emailUsuario ):

	""" 
		La funcion evualua un mail recibido en busca de arroba  
		
		Pruebas:
		>>> compruebaEmail('juan@cursos.es')
		True

		>>> compruebaEmail('@juancursos.es')
		False

		>>> compruebaEmail('juancursos.es@')
		False

		>>> compruebaEmail('juancursos.es')
		False
		
		>>> compruebaEmail('juan@@cursos.es')
		False
	"""

	arroba = emailUsuario.count('@')

	if arroba != 1 or emailUsuario.rfind('@') == ( len( emailUsuario ) - 1 ) or emailUsuario.find('@') == 0:
		return False
	
	else:
		return True	

import doctest as test
test.testmod()