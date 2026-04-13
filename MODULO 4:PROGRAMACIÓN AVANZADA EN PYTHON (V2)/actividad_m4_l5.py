

#1. Captura básica de errores
#• Escribe un programa que pida al usuario dividir dos números.
#Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable.
#2. Múltiples excepciones
#• Agrega validación para que el usuario ingrese solo números.
#Usa un bloque try/except con múltiples excepciones (ZeroDivisionError, ValueError).

""" 
print("======Division de 2 Numeros=====")
try:
    numero1= int(input("ingrese numero 1: "))
    numero2= int(input("ingrese numero2:"))
    resultado= numero1/numero2
    print(f"El resultado es:{resultado}")

except SyntaxError:
    print("error de sistaxis en python")
except ValueError:
    print("Por favor ingresar solo numeros")
except ZeroDivisionError:
    print("no se puede  dividir por 0 ") """



#3. Excepciones personalizadas
#• Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad
#es menor que 0.
#Define esta excepción como clase hija de Exception.

class EdadInvalidaError(Exception):
 
 pass 

def validar_edad(edad):
        if edad < 0:
         raise EdadInvalidaError(f"La edad no puede ser negativa:")
        else:
            print(f"La edad es correcta")   

try:
 edad= int(input("Ingrese una edad:"))
 validar_edad(edad)

except ValueError:
   print(f"Por favor ingresar solo numeros") 
    
 
            