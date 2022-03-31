alfabeto=("AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz")
texto=str(input("Digite la palabra: "))
contar=0

for i in texto:
    if i in alfabeto:
        contar+=1
    else:
        print("Se ha encontrado caracteres NO alfabeticos")
        break
if contar==len(texto):
    print("Todos los caracteres son alfabeticos ")   