#funcion
def mercado(frutas1,cadena1,ordenar1):
    contar=1
    for i in frutas1:
        print(f'{contar}. {i}')
        contar+=1
    print(f'\n\t°Cadena° \n{cadena1}')
    print(f'\n\t°ordenar°\n{ordenar1}')
    while True:
        buscador=input('\ndigite el producto que desea buscar  : ')
        if buscador in frutas_verduras:
            print(f'\n°resultado°\n{buscador}')
        else:
            print('el producto no existe\npara salir (S/s)')
        if buscador=='s' or buscador=='S':
            break
#programa principal
frutas_verduras=["manzana", "pera", "zanahoria", "pan","gaseosa","fresas","lentejas","maizpira","trigo","pasta"]
cadena=", ".join(frutas_verduras)
ordenar=sorted(frutas_verduras)
mercado(frutas_verduras,cadena,ordenar)
