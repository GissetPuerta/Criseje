text = str(input("inserte una palabra: "))

for char in text:
    if not char.isalpha():
        print('se han encontrado caracteres no alfabeticos!')
        break
else:
    print('sus caracteres son alfabeticos')
    