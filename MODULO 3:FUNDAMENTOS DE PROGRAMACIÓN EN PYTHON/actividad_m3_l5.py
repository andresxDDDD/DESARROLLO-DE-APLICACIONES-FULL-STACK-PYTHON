 #1 crear estructuras

nombres=["juan","marcos","celeste"] #lista tipo de dato que permite almacenar cualquier tipo de datos
numeros=(1,2,4,5) #tupla tipo de dato parecido a una lista pero los datos no se pueden modificar
paises=set({"chile","marruecos","india"})# tipo de dato que no se puede modificar, son unicos, son desordenados
producto={
    "nombre": "Jurel",
    "procedencia" : "chile",
    "peso":"3 kg",  #diccionario coleccion de elementos donde tiene una clave y un valor
}

print(nombres)
print(numeros)
print(paises)
print(producto)

print("-----------o---------------")

#2 acceder a elementos 

print(nombres[1]+": imprimiendo el segundo dato de la lista")

print("nombre:",producto["nombre"]+" :imprimiendo clave y valor del diccionario")

 #no se puede acceder a un set por indice por que los set no tienen indice. 

print("-----------o---------------")

#3 contar e iterar 
print("contando elementos")
print("hay "+ str(len(nombres))+" elementos en la lista")
print("hay "+ str(len(numeros))+" elementos en la tupla")
print("hay "+ str(len(paises))+" elementos en el set")
print("hay "+ str(len(producto))+" elementos en el diccionario")

print("---------o------------")

print("imprimiendo los datos de las estructuras")
for i in nombres:
    print(i)
    

for i in numeros:
    print(i)

for i in paises:
    print(i)    

for i, k in producto.items():
    print(i,k)    


#4 Modificar estructuras
print("-----------o-------------")
print("agregando y eliminado datos de la lista")
nombres.append("gloria") 
print(nombres)   

nombres.remove("gloria")
print(nombres)
print("-----------o-------------")
print("agregando datos al diccionario")

producto.update({
    "ciudad":"Punta arenas",
})
for i, k in producto.items():
    print(i,k)

""" numeros[0]= 10  """   #intentando modificar una dupla arroja error