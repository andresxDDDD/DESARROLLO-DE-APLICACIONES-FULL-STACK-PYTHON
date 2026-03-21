#1.	Uso básico de while

""" numero=1
while numero <=5:
    print(numero)
    numero+=1 """
      
#2.	Uso básico de for

""" frutas=["manzana","platano","naranja"]  
for i in frutas:
    print(i)  """   
   
#3.	Condición en un ciclo
""" numero=1
num_lis=[]
while numero <=10:
 num_lis.append(numero)
 numero+=1
 
for i in num_lis:
    if i % 2 == 0: 
       print(f"{i} es numero  par")
    else:
       print(f"{i} es numero  impar")  """  
        
#4.	Ciclo infinito controlado con break

""" while True: 
    num=int(input("ingrese un numero para salir escriba un 0 :"))
    if num == 0: 
        break """

#5.	Ciclo anidado
""" numero=1
mul_lis=[]
fac_lis=[1,2,3]

while numero <=10:
 mul_lis.append(numero)
 numero+=1

for i in fac_lis:
    print("-------------")
    for k in mul_lis:
       factor=i*k
       print(i,"x",k,"=",factor)
     """

#6. Uso de continue

""" lis_nom=["Jorge","Cristian","Juan","Rocio","Gabriel"]
for i in lis_nom:
    
    if i == "Juan":
        continue
    print(i)    
      """
