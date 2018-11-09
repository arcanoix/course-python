# verificador de email

print("========================================")

print("Verificador de Email")

print()

miEmail=input("Introduce tu dirección de email: ")

verificacion=miEmail.partition("@") # convierte el correo en una tupla de tres elementos, usando como referencia el arroba

parte_local,arroba,dominio=verificacion # se iguala cada elemento de la tupla "verificacion" con una variable

contador=0


caracteres_no=[" ", "@","\"", "#", "$", "$", "!", "/", "(", ")","=", "?", "¿", "°","%"  ]

for i in miEmail:
	if(i=="@" ):
		contador=contador+1

if contador==1  and len(parte_local)<=64 and len(dominio)<=254 and dominio==dominio.lower():
	for i in (parte_local+dominio):
		if  i in  caracteres_no:
			print("El email no es correcto")
			break;
		else:
			print("El email es correcto")
else:
	print("El email no es correcto")﻿