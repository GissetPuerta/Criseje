asistentes = 0
hombres = 0
mujeres = 0
edades_hombres = []
edades_mujeres = []
repetir = 's'
edad = 1

while repetir=='s' or repetir=='S':
    print ('cls')
    genero = 0
    edad = int (input ('Ingresa el valor de edad: '))
    if edad<18:
        print ('No se permiten menores de edad a la fiesta.')    
    else:
        asistentes+=1
        print ('Selecciona el valor de genero.')
        print ('\t1.- Mujer')
        print('\t2.- Hombre')
        while genero not in [1,2]:
            genero = int (input (': '))
            if genero not in [1,2]:
                print ('Valor incorrecto. Ingresalo nuevamente.')
        if genero==1 and edad>=18:
            mujeres+=1
            edades_mujeres += [edad]
        if genero==2 and edad>=18:
            hombres+=1
            edades_hombres += [edad]
    if edad != 0:
        repetir = str(input('Deseas repetir el proceso? (S/N):'))
    else:
        break

print('Personas que asistieron a la fiesta:',hombres+mujeres)
print('Número de hombres:', hombres)
print('Número de mujeres', mujeres)
if len(edades_hombres) > 0:
    print('Edad promedio hombres',sum(edades_hombres)/len(edades_hombres))
if len(edades_mujeres) > 0:
    print('Edad promedio mujeres',sum(edades_mujeres)/len(edades_mujeres))
print('Edad de la persona más joven',min(edades_hombres+edades_mujeres))