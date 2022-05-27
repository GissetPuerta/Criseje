class Coche:
    color="Rojo"
    marca="Ferari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    motor=2600
    
#métodos
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color 
    def acelerar(self):
        
        self.velocidad+=1
    
    def frenar(self):
        
        self.velocidad-=1
    def getVelocidad(self):
        
        return self.velocidad
    #instanciar la clase
print("Valores de la clase antes de llamar los metodos")
coche1= Coche()
print(coche1.marca,coche1.color,coche1.caballaje)
print("Velocidad actual:",coche1.getVelocidad())
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()
print("COCHE 1 despues de llamar los métdos")
print("Velocidad nueva:",coche1.velocidad)
coche1.setColor("negro")
print("El nuevo color del carro es:",coche1.getColor())
#creando otro objeto
coche2=Coche()
print("COCHE 2")
print(coche2.getColor())
coche2.setColor("Amarrillo")
print("El nuevo color del carro es:",coche2.getColor())