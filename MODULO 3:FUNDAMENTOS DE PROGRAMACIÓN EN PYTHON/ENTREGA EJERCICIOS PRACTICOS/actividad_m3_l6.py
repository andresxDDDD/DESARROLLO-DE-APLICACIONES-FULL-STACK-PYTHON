# ejercicio 1: Al ingresar un numero par cualquiera que sea del 2 al 100, 
# este imprima en pantalla todos los números pares siguientes,
#  y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en pantalla 
# todos los números impares siguientes hasta el 99.
#Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa debe enviar un 
#mensaje de que no es posible realizarlo y volver a preguntar por el ingreso del número. 

""" while True:
    numero= int(input("Ingrese un numero  menor a 100: "))

    if numero > 0 and numero <101:

             if numero % 2 == 0:
                    print("Estos son los numero pares a partir del numero ingresado") 
                    for i in range(numero,101,2):
                        print(f"{i}")
                    break      
             else:
                    print("Estos son los numero impares a partir del numero ingresado")
                    for i in range(numero,101,2):
                         print(f"{i}")
                    break     
                
    else:

        print("No es posible realizar el calculo")  
 """


#ejercicio 2: Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
#0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado
#y la menor.
""" import os
def limpiar_pantalla():
     os.system('cls' if os.name == 'nt' else 'clear') 
notas= []   
while True:

     

    print("-------------Menu-----------") 
    print("1- Ingreso de notas")
    print("2- Mostrar las notas")
    print("3- Mostrar nota media")
    print("4- Mostrar la nota mas alta")
    print("5- Mostrar la nota mas baja")
    print("6- Salir")

    opcion= int(input("Ingrese una opcion: "))
    
    
    
    if opcion ==1:
      
      limpiar_pantalla()
      if len(notas) < 5:
          for i in range(5):
                    if len(notas) >= 0 and len(notas)<5:
                              nota= int(input("Ingrese Nota:"))
                              if nota >= 0 and nota <= 10 :
                               notas.append(nota)
                              else:
                                   print("ingrese una nota entre 0 y 10. la nota no ha sido grabada ")
      else:              
           print("notas ya ingresadas")      
     
                                  
     
            
            
    elif opcion ==2:
            limpiar_pantalla()
            if len(notas) > 0 and len(notas)>=5:
          
                 print(notas)
            else:
                 print("No hay notas disponibles o faltan notas")
    elif opcion == 3:
            limpiar_pantalla()
            if len(notas) > 0 and len(notas)==5:
                nota_media= sum(notas)/len(notas)  
                print("La nota media",nota_media)  
            else:
                 print("No hay notas disponibles o faltan notas")
    elif opcion == 4 :
         limpiar_pantalla()
         if len(notas) > 0 and len(notas)==5:
            nota_alta= max(notas) 
            print("la nota mas alta es:",(nota_alta))  
         else:
                 print("No hay notas disponibles o faltan notas")              
    elif opcion == 5 :
         limpiar_pantalla()
         if len(notas) > 0 and len(notas)==5:
            nota_baja= min(notas) 
            print("la nota mas baja es:",(nota_baja)) 
         else:
                 print("No hay notas disponibles o faltan notas") 

    elif opcion <=0 or opcion >6:
        limpiar_pantalla()
        print("Ingresa una opcion valida")
    elif opcion == 6: 
         break                         """

#ejercicio3: Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga 
#cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos 
#a suponer que febrero tiene 28 días. 


""" meses = [{"mes":1,"nombre":"Enero","dias": 31},{"mes":2,"nombre":"Febrero","dias":28},{"mes":3,"nombre":"Marzo","dias":31}
         ,{"mes":4,"nombre":"Abril","dias":30},{"mes":5,"nombre":"Mayo","dias":31}
         ,{"mes":6,"nombre":"Junio","dias":30},{"mes":7,"nombre":"Julio","dias":31}
         ,{"mes":8,"nombre":"Agosto","dias":31},{"mes":9,"nombre":"Septiembre","dias":30},
         {"mes":10,"nombre":"Octubre","dias":31},{"mes":11,"nombre":"Noviembre","dias":30},{"mes":12,"nombre":"Diciembre","dias":31}]
    
opcion= int(input("Ingrese un numero de mes:"))

for i in meses:
    if i["mes"]== opcion:
        print(f"El mes {i['nombre']} tiene {i['dias']} días.")
         """