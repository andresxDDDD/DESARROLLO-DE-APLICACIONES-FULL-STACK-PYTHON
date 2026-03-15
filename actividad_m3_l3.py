#1- decision simple
""" edad = input("Ingrese una edad:")
if edad >="18":
    print(" Eres mayor de edad")
elif edad <"18": 
    print("Eres menor de edad ") """


#decision multimple con elif
""" while True:
    numero= input("Ingrese una calificacion entre 1 y 7:")

    if numero == "7":
        print("Su calificacion es Excelente")
    elif numero =="6":
        print("Su calificacion es Muy bien")    
    elif numero=="5":
        print("Su calificacion es Buena")     
    elif numero=="4":
        print("Su calificacion es Suficiente") 
    elif numero < "4":
        print("Su calificacion es Insuficiente") 
    else:
        break      """


#decisiones anidadas
""" num_entero = input("Ingrese un numero:")
if num_entero !="0":
    if num_entero >"0":
        print("Numero Positivo")
    elif num_entero <"0":
        print("Numero negativo") 
        
else: 
    print("El numero es 0 ") """


#condiciones de borde
""" num_borde= int(input("Ingrese un numero entre 1 y 100: "))
if num_borde ==1 or num_borde == 100: 
    print("Estas en el limite permitido")
elif num_borde > 1 and num_borde < 100: 
    print("Dentro del rango")    
else:
    print("Fuera del rango") """
