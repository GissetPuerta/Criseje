#ejemplo
lenguajes = ["Java", "C", "C++", "Rust", "Elixir"]
for i, lenguaje in enumerate(lenguajes, 1):
    print(i, lenguaje)
    
# venta de boletas
cedula=list()
contador=0

for i, cedula1 in enumerate(cedula, 1):
    cedula1=int(input('digite el número de la cedula: '))
    print(i, cedula1)

#cedula
cedula_i=list()
contador=0
cedula=0

for i in range(1,101):
    ingrese=int(input('sdigite el número de la cedula: '))
    cedula_i.append(ingrese)
    print(contador,cedula_i)
    
    for contador, direccion in enumerate(direcciones, start=1):
	print(contador, direccion)