salarioPresidente = int( input( "\nIntroduce el salario del presidente: " ) )
salarioDirector = int( input( "Introduce el salario del director: " ) )
salarioJefeArea = int( input( "Introduce el salario del Jefe de Area: " ) )
salarioAdministrativo = int( input( "Introduce el salario del Administrativo: " ) )

print( "\nSalario presidente: " + str( salarioPresidente ) )
print( "Salario director: " + str( salarioDirector ) )
print( "Salario jefe de area: " + str( salarioJefeArea ) )
print( "Salario administrativo: " + str( salarioAdministrativo ) + "\n")

# concatenacion de signos de comparacion

if salarioAdministrativo < salarioJefeArea < salarioDirector < salarioPresidente:
	print( "Todo bien\n" )

else: 
	print( "Revisar la nomina\n" )