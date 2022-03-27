ne=input("ingrese el nombre del estudiante: ")
ef=float(input("ingrese la nota de la evaluacion final: "))
q1=float(input("ingrese la nota del quiz1: "))
q2=float(input("ingrese la nota del quiz2: "))
q3=float(input("ingrese la nota del quiz3: "))
tf=float(input("ingrese la nota del trabajo final: "))
qz=(q1+q2+q3)/3
nf= ef*0.5 + qz*0.2 + tf*0.3
print("Nombre del estudiante: ",ne, ";la nota final es: ",nf)