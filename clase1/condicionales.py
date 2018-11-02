#condicionales 1

print("Programa de evaluacion de notas")

nota_alumno = input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))