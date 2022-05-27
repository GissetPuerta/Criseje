#funcion principal
def registroEstudiante(registro,llave,valor):
    while True:
#se crea un menú para elegir la opcion que desee.
        print('\n---------------------\nMy Second Home School\n\nSeleccione la opcion a consultar\n')
        print('[1]Ingresar estudiantes\n[2]Listar estudiante\n[3]Modificar notas\n[4]Consultar nota definitiva\n[S/s]Salir-->\n')
#se pide por pantalla la opcion.
        opcion=input('Digite una opcion : ')
#opcion para salir del programa.
        if opcion<='0' or opcion>='5':
            print('\n|La opcion es incorrecta, digite una opcion valida|')
        if opcion=='s' or opcion=='S':
            break
        if opcion=='1':
            print('\n\t|Registro estudiante|\n')
#opcion 1 se pide el registro del estudiante, (codigo, nombre, nota1, nota2)
            codigo=int(input('Digite el codigo : '))
            if codigo in registro:
                print('\n|codigo existente|')
                continue
            nombre=str(input('Digite el nombre : '))
            nota1=float(input('Digite la nota (1) : '))
            if nota1>5:
                print('la nota debe oxcilar entre 0.0 y 5.0')
                continue
            nota2=float(input('Digite la nota (2) : '))
            if nota2>5:
                print('la nota debe oxcilar entre 0.0 y 5.0')
                continue
#la informacion se almacenara en un diccionario donde la clave que es el (codigo) y los valores (nombre, nota1, nota2)
            registro[codigo]=[nombre,nota1,nota2]
            print(f'\n¡Registro Exitoso! {registro}')
#opcion 2 se tabula o lista la informacion de los estudiantes.
        if opcion=='2':
            print('\n\t|Lista estudiante|\n')
            print('{:<13}{:<13}{:<13}{:<13}'.format('Codigo','Nombre','Nota 1','Nota 2'))
            for i,j in zip(llave,valor):
                codigo=i
                nombre,nota1,nota2=j
                print('{:<13}{:<13}{:<13}{:<13}'.format(codigo,nombre,nota1,nota2))
#opcion 3 se muestra la informacion de los estudiantes y cambiar notas (nota1, nota2).
        if opcion=='3':
            print('\n\t|Modificar nota|\n')
            print('{:<13}{:<13}{:<13}{:<13}'.format('Codigo','Nombre','Nota 1','Nota 2'))
            for i,j in zip(llave,valor):
                codigo=i
                nombre,nota1,nota2=j
                print('{:<13}{:<13}{:<13}{:<13}'.format(codigo,nombre,nota1,nota2))
            #se pide por pantalla el codigo del estudiante para cambiar una o ambas notas definitivas.
            modificar1=int(input('\nDigite el codigo del estudiante : '))
            if modificar1 in registro[modificar1]:
                pass
            print('\n|Seleccione la nota a modificar|')
            print('\n[1]Modificar Nota 1\n[2]Modificar Nota 2\n[3]Modificar Nota 1 y Nota 2')
            nueva_nota=int(input('\nDigite la opcion de la nota a modificar : '))
            #opcion 1 si desea cambiar Nota n°1
            if nueva_nota==1:
                nota_1=float(input('\nDigite una nueva Nota 1 {}: '.format(registro[modificar1][0])))
                if nota_1<=5:
                    print('Nota n°1 cambiada exiosamente')
                if nota_1>5:
                    print('la nota debe oxcilar entre 0.0 y 5.0')
                    continue
                registro[modificar1][1]=nota_1
                continue
            #opcion 2 si disea cambiar la Nota n°2
            if nueva_nota==2:
                nota_2=float(input('\nDigite una nueva Nota 2 {}: '.format(registro[modificar1][0])))
                if nota_2<=5:
                    print('Nota n°2 cambiada exiosamente')
                if nota_2>5:
                    print('la nota debe oxcilar entre 0.0 y 5.0')
                    continue
                registro[modificar1][2]=nota_2
                continue
            #opcion 3 si desea cambiar ambas notas (Nota n°1, Nota n°2)
            if nueva_nota==3:
                nota_1=float(input('\nDigite una nueva Nota 1 de {}: '.format(registro[modificar1][0])))
                if nota_1<=5:
                    print('Nota n°1 cambiada exiosamente')
                if nota_1>5:
                    print('la nota debe oxcilar entre 0.0 y 5.0')
                    continue
                nota_2=float(input('Digite una nueva Nota 2 de {}: '.format(registro[modificar1][0])))
                if nota_2<=5:
                    print('Nota n°2 cambiada exiosamente')
                if nota_2>5:
                    print('la nota debe oxcilar entre 0.0 y 5.0')
                    continue
                registro[modificar1][1]=nota_1
                registro[modificar1][2]=nota_2
                continue
#opcion 4 se muestra la informacion de los estudiantes y poder observar su respectivo codigo.
        if opcion=='4':
            print('\n\t|Nota definitiva|\n')
            print('{:<13}{:<13}{:<13}{:<13}'.format('Codigo','Nombre','Nota 1','Nota 2'))
            for i,j in zip(llave,valor):
                codigo=i
                nombre,nota1,nota2=j
                print('{:<13}{:<13}{:<13}{:<13}'.format(codigo,nombre,nota1,nota2))
            #se pide por patalla el codigo del estudiante y observar su promedio final.
            nota_definitiva=int(input('\nDigite el codigo del estudiante : '))
            if nota_definitiva in registro[nota_definitiva]:
                pass
            print('\n|Promedio final|\n')
            print('{:<13}{:<13}'.format('Nombre','promedio'))
            print('{:<13}{:<13}'.format(registro[nota_definitiva][0],(registro[nota_definitiva][1] + registro[nota_definitiva][2])/2))
#programa principal.
registro=dict()
llave=registro.keys()
valor=registro.values()
registroEstudiante(registro,llave,valor)