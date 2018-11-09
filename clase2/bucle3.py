#for i in range(5,10):
	# si le decimos range(5,10) es que emmpieza en 5 y terminar en 9
	#si le decimos range(5,50,3) es que empieza en 5 hasta 50 contando de 3 en tres
	#la f es una anotacion para unir texto y variables
	#print(f"valor de la variable {i}")


valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True


if valido:
	print("Email correcto")
else:
	print("Email Incorrecto")