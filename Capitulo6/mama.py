meses=['enero','febreo','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
produccion=list()
for i in meses:
    produccion_cafe=int(input(f'digite la produccion de cafe del mes de {i} : '))
    produccion.append(produccion_cafe)
promedio=sum(produccion)/len(meses)
mayor=max(produccion)
minimo=min(produccion)
diccionario=dict(zip(meses,produccion))
print(f'\nmeses_produccion : {diccionario}\n\npromedio : {promedio:.2f}\nmayor produccion : {mayor}\nmenor produccion : {minimo}')