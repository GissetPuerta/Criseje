cantidad_restante=5
cantidad_total=0
hombre=0
mujer=0
lista_ID=list()
lista_nueva=list()
for i in range(1,11):
#cuando la cantidad llegue a cero muestre un mesaje y finalice
    if cantidad_restante==0:
        print("\n\t---Boletas agotadas---")
        break
#años
    edad=int(input('\ndigite su edad : '))
    if edad>=18:
        lista_nueva.append(edad)
        print('aceptado')
    if edad<=17:
        print('alerta')
        break
#genero
    genero=str(input("digite su genero (f/m): "))
    if genero=='m':
        hombre+=1
    if genero=='f':
        mujer+=1

#presentar cedula de 
    print('\n\t---Venta de boletas en línea---\n')
    ingrese_ID=int(input('\ndigite el numero de cedula  : '))
#si el documento existe rechazar la venta de la boleta
    if ingrese_ID not in lista_ID:
        print("Documento registrado\n\n\t---Bienvenido a la compra de su boleta en línea---")
#agregar cedula de ciudadania a un vector
        lista_ID.append(ingrese_ID)
#cantidad de boletas que desea comprar
        while True:
            print(f'\ncantidad de boletas disponibles : {cantidad_restante}')
            venta_boleta=int(input('digite la cantidad de boletas que desea comprar : '))
#intenta nuevamente si es mayor a (4) cantidad de boletas
            if cantidad_restante<venta_boleta and cantidad_restante!=0:
                print('la cantida excede')
                continue
#la cantidad es correcta si es menor a (4)
            if venta_boleta<=4:
                cantidad_restante-=venta_boleta
                cantidad_total+=venta_boleta
                print("su compra ha sido exitosa")
                break
    else:
        print("el documento ya existe")
print(f'\nLista_ID: {lista_ID}\ncantidad de boletas disponibles: {cantidad_restante}\ncantidad de boletas compradas: {cantidad_total}')
print(f"Los hombres que asistieron al concierto son:{hombre}\nlas mujeres que asistieron al concierto son: {mujer}")