tex= str(input("Digite el una oración: "))          
tex= tex.upper()
listTex= tex.split(" ")
list1=list(set(listTex))
print(list1)