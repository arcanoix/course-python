#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
#teclado)

print("Bienvenido al sistema")

nombre=input("introduce tu nombre: ")
direccion = input("introduce la direccion: ")
telefono = input("Introduce el telefono: ")

nuevalista=[nombre, direccion, telefono]


print("los datos personales son nombre"+ nuevalista[0]+ " Direccion: "+ nuevalista[1]+ " telefono: "+ nuevalista[2])

print("ha finalizado el programa")