class Cuenta:
#atributos numero, fecha apertura, saldo. en constructor.
    def __init__(self,numero,fecha_apertura,saldo):
        self.numero = numero
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo
        
#metodo Retiro
    def retiro(self):
        print("\n                                                                      ")
        self.retiro=int(input(f'Digite el valor a retirar |su saldo total es de --> {self.saldo}| : '))
        if self.saldo>=self.retiro:
            return f'Su retiro fue ¡Exitoso! -- Saldo Total :{self.saldo-self.retiro}'
        else:
            return 'El valor que desea retirar es insuficiente'

#metodo consignar
    def consignar(self):
        print("\n                                                                          ")
        self.consignar=int(input(f'Digite el valor a consignar |su saldo total es de --> {self.saldo-self.retiro}|: '))
        return f'Su consignacion fue ¡Exitosa! -- {self.saldo-self.retiro+self.consignar}'
        
        

#informacion de la cuenta
    def informacion(self):
        print("\n                                                                 ")
        print('{:<25}{:<26}{:<22}'.format('Número de cuenta','Fecha de apertura','Saldo total'))
        return('{:<25}{:<26}{:<22}'.format(self.numero,self.fecha_apertura,self.saldo-self.retiro+self.consignar))

class cuentaCorriente(Cuenta):
    def __init__(self, numero, fecha_apertura, saldo,cheque):
        super().__init__(numero, fecha_apertura, saldo)
        self.cheque=cheque
    def corriente(self):
        return f'El numero de cheque es --> {self.cheque}'

cuenta1=Cuenta(1234,'19/noviembre/2019',1000000)
print(cuenta1.retiro())
print(cuenta1.consignar())
print(cuenta1.informacion())
print("\n                                                                       ")
print("|Cuenta corriente|")
corriente1=cuentaCorriente(5678,'20/julio/2019',1000000,1125)
print(corriente1.retiro())
print(corriente1.consignar())
print(corriente1.informacion())
print(corriente1.corriente())