
#1. Definición de una clase con constructor
#crea una clase Libro con los atributos titulo, autor y anio_publicacion.
#• Define un método constructor __init__() que inicialice esos atributos.
#• Crea un método mostrar_info() que imprima los datos del libro.

""" class Libro:
     
    def __init__(self,titulo,autor,anio_publicacion):
            self.titulo = titulo
            self.autor = autor
            self.anio_publicacion = anio_publicacion

    def mostrar(self):
        return f"{self.titulo} - {self.autor} - {self.anio_publicacion} "  
    
    def __str__(self):
         return f"Titulo:{self.titulo} - Autor:{self.autor} - Año publicacion:{self.anio_publicacion} "  

libro1 = Libro("Papelucho y el Marciano","Marcela paz",1968) 
print(libro1)  """

#2. Métodos accesadores y mutadores
#• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el 
#atributo titulo.
#• Repite lo mismo para el atributo anio_publicacion.
#• Usa estos métodos para modificar el título de un libro desde el programa principal


class Libro:
     
    def __init__(self,titulo,autor,anio_publicacion):
            self.__titulo = titulo
            self.autor = autor
            self.__anio_publicacion = anio_publicacion

    def mostrar(self):
        return f"{self.__titulo} - {self.autor} - {self.__anio_publicacion} "  
    
    def __str__(self):
         return f"Titulo:{self.__titulo} - Autor:{self.autor} - Año publicacion:{self.__anio_publicacion} "

    def get_titulo(self):
        return self.__titulo      
    
    def set_titulo(self,titulo_nuevo):
           self.__titulo = titulo_nuevo
        
    def get_anio_publicacion(self):
        return self.__anio_publicacion      
    
    def set_anio_publicacion(self,nuevo_anio):        
           self.__anio_publicacion= nuevo_anio

    def resumen(self,resumen= None): #3. Sobrecarga de métodos      
      if resumen:
            print(f"Resumen de '{self.__titulo}': {resumen}")
      else:
            print("Libro sin resumen disponible")    


libro1 = Libro("Papelucho y el marciano","Marcela paz",1968) 
print(libro1)
libro1.set_titulo("Dragon Ball") 
libro1.set_anio_publicacion(2026)
print(f"Nuevo título : {libro1.get_titulo()}")
print(f"Nuevo año: {libro1.get_anio_publicacion()}")
libro1.resumen("Dragon ball")

