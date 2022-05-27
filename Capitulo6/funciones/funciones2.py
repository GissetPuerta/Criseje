#funcion    
def lista(lista1):
    for i in range(10): 
        objetos=input('\ndigite el objeto que desea en la lista  : ')
        lista1.append(objetos)
    print(f"\n\tLos elementos de la lista son:\n")
    print(lista1)

#programa principal
lista1=list()
lista(lista1)