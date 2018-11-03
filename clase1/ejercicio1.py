#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.

def devuelvemax(n1, n2):
	total="ninguno"
	if n1<n2:
		total="N2 es mas alto que N1"
	elif n1>n2:
		total="N1 es mas alto que N2"
	else:
		total="son iguales"
	return total


print("Bienvenido al sistema")
num1=int(input("Introduce el numero 1: "))
num2=int(input("Introduce el numero 2: "))

print(devuelvemax(num1, num2))