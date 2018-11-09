import math
print("Programa de calculo de raiz cuadrada")

numero=int(input("Introduce un numero: "))

intento=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	if intentos==2:
		print("Has consumido demasiados intentos")
		break; #break es para finalizar el programa
	numero=int(input("Introduce un numero: "))
	if numero <0:
		intentos=intentos+1

if intentos<2:
	# math es una clase que estamos importando para el calculo matematico
	solucion=math.sqrt(numero)
	print("la raiz cuadrada de " + str(numero) + " es " + str(solucion))