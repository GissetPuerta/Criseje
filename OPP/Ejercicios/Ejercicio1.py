class aprendiz: 
    id=1000535332
    nombre="Gisset Cristina Calderon"
    edad=19
    correo="gisset@gmail.com"
    telefono= 3107733080
    
#metodos

    def setId(self,id):
        self.id= id
    def getId(self):
        return self.id
    
    def setNombre(self,nombre):
            self.nombre=nombre
    def getNombre(self):
        return self.nombre  
    
    def setEdad(self,edad):
            self.edad=edad
    def getEdad(self):
        return self.edad
    
    def setCorreo(self,correo):
        self.correo=correo
    def getCorreo(self):
        return self.correo 
    
    def setTelefono(self,telefono):
        self.telefono=telefono
    def getTelefono(self):
        return self.telefono
    
    def calcularEdad(self,edad):
        if edad>=18:
            print("El aprendiz es mayor de edad")
        else:
            print("El aprendiz es menor de edad")
            
    #instanciar la clase

print(f"\n\t\nDatos del aprendiz antes de modificarlos")
aprendiz1=aprendiz()
print(f"\nEl id del aprendiz es:{aprendiz1.id},\nEl nombre del aprendiz es: {aprendiz1.nombre},\nLa edad del aprendiz es: {aprendiz1.edad},\nEl correo del aprendiz es:{aprendiz1.correo},\nEl telefono del aprendiz es: {aprendiz1.telefono}")

#Objeto aprendiz 1
aprendiz1.setId(1001058687)
aprendiz1.setNombre("Ani Cruz")
aprendiz1.setEdad(20)
aprendiz1.setCorreo("anicruz0824@gmail.com")
aprendiz1.setTelefono(3143565157)
print(f"\n\t\nDatos del aprendiz 1 modificados: \n")
print(f"\nEl id del aprendiz 1 es: {aprendiz1.getId()},\nEl nombre del aprendiz 1 es: {aprendiz1.getNombre()},\nLa edad del aprendiz 1 es: {aprendiz1.getEdad()},\nEl correo del aprendiz 1 es: {aprendiz1.getCorreo()},\nEl telefono del aprendiz 1 es: {aprendiz1.getTelefono()}\n ")
aprendiz1.calcularEdad(20)

#objeto aprendiz 2
aprendiz2=aprendiz()

aprendiz2.setId(1005815023)
aprendiz2.setNombre("Steven Lozano")
aprendiz2.setEdad(16)
aprendiz2.setCorreo("brx32z@gmail.com")
aprendiz2.setTelefono(3197161874)
print(f"\n\t\nDatos del aprendiz 2 modificados: \n")
print(f"\nEl id del aprendiz 2 es: {aprendiz2.getId()},\nEl nombre del aprendiz 2 es: {aprendiz2.getNombre()},\nLa edad del aprendiz 2 es: {aprendiz2.getEdad()},\nEl correo del aprendiz 2 es: {aprendiz2.getCorreo()},\nEl telefono del aprendiz 2 es: {aprendiz2.getTelefono()}\n ")
aprendiz1.calcularEdad(16)