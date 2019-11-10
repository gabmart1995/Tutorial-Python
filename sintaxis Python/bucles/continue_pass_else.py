# pass
class MiClase:
	pass	# permite el desarrollo de la misma para más tarde

# continue
nombre = "Pildoras Informaticas"

contador = 0

for letra in nombre:
	
	if letra == " ":
		continue  # pasa a la siguente iteracion

	contador += 1

print( contador )

# else puede usarse en for se ejecuta cuando el bucle este vacio

email = input( "introduce tu email: " )

for i in email:

	if i == '@':
		arroba = True
		break

else:
	arroba = False

print( arroba )