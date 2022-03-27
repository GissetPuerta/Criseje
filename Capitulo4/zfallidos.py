tecla1 = "win"
tecla2 = "alt"
tecla3 = "ctrl"
#windows
tw1 = "g"
tw2 = "c"
tw3= "a"
tw4= "d"
w= (tw1, tw2, tw3)
#ALlt
ta1= "tabulador"
ta2= "f4"
a= (ta1, ta2)
#Ctrl
tc1= "c"
tc2= "v"
tc3= "a"
c= (tc1, tc2, tc3)

if tecla1==tw1:
    print("Abre la barra de juegos")
elif tecla1==tw2:
    print ("haz que aparezca cortana")
elif tecla1==tw3:
    print("abre las notificaciones")
elif tecla1== tw4:
    print ("muestra el escritorio")
elif tecla2==ta1:
    print ("abre el conmutador de tareas")
elif tecla2==ta2:
    print ("f4")
elif tecla3 ==tc1:
    print ("copiar")
elif tecla3== tc2:
    print ("pegar")
elif tecla3 ==tc3:
    print ("Seleccionar todo")