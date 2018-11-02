# las tuplas se crean con ()

nuevatupla = ("dairy","gustavo","megan")
nuevalista =["dairy","gustavo"]
# convertir una tupla en lista
milista =list(nuevatupla)

#convertir lista  a tupla
mitupla=tuple(nuevalista)

# se recorre con [:]
print(nuevatupla[:])

print(nuevatupla[0])

# se imprime en [] lo que se convirtio en tupla a lista
print(milista)

# se imprime en () lo que se convirtio de lista a tupla
print(mitupla)

#buscar valor en tupla
print("dairy" in mitupla)

#contador de elementos existente en la tupla
print(mitupla.count("dairy"))

#contador de elementos de la tupla
print(len(mitupla))

#tuplas unitarias
m1tupla =("Gustavo",)
print(len(m1tupla))

#empaquetado de tupla
tupladiferente="gustavo",12,1
print(tupladiferente)

#desempaquetado de tupla
mitupla2=("gustavo", 23, 12, 1984)
#se coloca cada variable en su posicion
nombre, dia, mes, agno=mitupla2

print(nombre)
print(dia)
print(mes)
print(agno)