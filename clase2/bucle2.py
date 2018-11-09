#for i in ["Java","Php","Python"]:
#el argumento end="" es para colocar la impresion sin espacio en blanco
#	print("Hola", end=" ")

# for i in "HolaMundo@app.com"
# este codigo recorre el ciclo por cada caracter existente



#programa para verificar si el email es correcto
contador=0
miemail = Input("Introduce tu direccion de email: ")
#Se recorre en vez de lista es un string, recorre cada caracter
for i in miemail:
	#verifica si i vale @ si encuentra ese simbolo y se declara Verdadero
	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:
	print("email correcto")
else:
	print("Email no es correcto")   



# for i in range(5):
#   print("Hola")
# range es un tipo corre un bucle 5 veces

