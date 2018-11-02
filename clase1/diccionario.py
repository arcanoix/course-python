#diccionario es valor:clave

#crearemos un diccionario paises
midiccionario={"Alemania":"Berlin", "Francia":"Paris","Venezuela":"Caracas"}

#devolveremos el valor asignado a esa clave
print(midiccionario["Francia"])

#imprimir diccionario
print(midiccionario)

#agregar elementos a un diccionario
midiccionario["Peru"]="Lisboa"
# corregir 
midiccionario["Peru"]="Lima"

print(midiccionario)

#eliminar un elemento se usa del diccionario["valor"]

del midiccionario["Alemania"]

print(midiccionario)

# cargar un diccionario desde una tupla
mitupla=["espania", "francia", "Alemania"]
midicc ={mitupla[0]:"Madrid", mitupla[1]:"francia",mitupla[2]:"Londres"}

print(midicc)

# algo diferente

personaje={23:"Jordan", "nombre":"michael","equipo":"chicago","anillo":{"temporadas":[1991,1992,1995]}}

#buscar valor de una clave
print(personaje["equipo"])

#
print(personaje["anillo"])

print(personaje.keys())
print(personaje.values())
print(len(personaje))