#funcion.
def serieFibonacci(listaFib):
    a = 0
    b = 1
    for i in range(1):
        fib1=int(input('\nDigite el numero : '))
    listaFib.append(1)
    for x in range(fib1-2):
        c = b+a
        a = b
        b = c
        listaFib.append(c)
    print(f"\n\tLos elementos en la lista Fibonacci son: \n")
    print(listaFib)
    
#programa principal
listaFib=list()
serieFibonacci(listaFib)