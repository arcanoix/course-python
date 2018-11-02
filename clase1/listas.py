nuevoarray=["dairy","gustavo","megan",'Peru']


#agregar valor al array
nuevoarray.append("nuevesito")

#agregar valor en una posicion indicada
nuevoarray.insert(2,"Python")

#agregar varios valores al array
nuevoarray.extend(["js","php"])

#eliminar un elemento del array
nuevoarray.remove("js")

#eliminar el ultimo de la lista
nuevoarray.pop()

# se recorre todo el array con [:]
print(nuevoarray[:])

# seleccionar el indice 1 gustavo 
print(nuevoarray[1])

#acceder a una porcion del array ["dairy","gustavo","megan"]
print(nuevoarray[0:3])

# es igual hacer sobreentiende que el primero es 0
print(nuevoarray[:3])
#del primero hasta el final
print(nuevoarray[1:])

#como saber en que posicion del indice se encuentra el valor
print(nuevoarray.index("dairy"))

#comprobar si un elemento se encuentra en el array
print("node" in nuevoarray)

#como unir dos array en una
nuevoarray2=["visual","css"]

nuevoarray3=nuevoarray+nuevoarray2

# modo repetidor vector imprimir 3 veces
nuevalista = ["valor 1", "valor2"] * 3

print(nuevalista[:])

print(nuevoarray3[:])