#While bucle

#i=1

#while i<=10:
	#print("hola "+ str(i))
	#i=i+1

#print("Termino la ejecucion")

edad=int(input("Introduzca la edad: "))

while edad<5 or edad>100:
	print("Edad Incorrecta")
	edad=int(input("Introduzca la edad: "))

print("Gracias por participar")
print("Edad del aspirante: " + str(edad))