
#1. Definición de una clase con constructor
#crea una clase Libro con los atributos titulo, autor y anio_publicacion.
#• Define un método constructor __init__() que inicialice esos atributos.
#• Crea un método mostrar_info() que imprima los datos del libro.

""" class Libro:
     
    def __init__(self,titulo,autor,anio_publicacion):
            self.titulo = titulo
            self.autor = autor
            self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        return f"Titulo:{self.titulo} - Autor:{self.autor} - Año publicacion:{self.anio_publicacion} "  
    
    
libro1 = Libro("Papelucho y el Marciano","Marcela paz",1968) 
print(libro1.mostrar_info()) """








#2. Métodos accesadores y mutadores
#• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el 
#atributo titulo.
#• Repite lo mismo para el atributo anio_publicacion.
#• Usa estos métodos para modificar el título de un libro desde el programa principal


""" class Libro:
     
    def __init__(self,titulo,autor,anio_publicacion):
            self.__titulo = titulo
            self.autor = autor
            self.__anio_publicacion = anio_publicacion

    def mostrar_info(self):
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
print(libro1.mostrar_info())
libro1.set_titulo("Dragon Ball") 
libro1.set_anio_publicacion(2026)
print(f"Nuevo título : {libro1.get_titulo()}")
print(f"Nuevo año: {libro1.get_anio_publicacion()}")
libro1.resumen("Dragon ball")
print(libro1.mostrar_info()) """









#4. Colaboración entre objetos
#• Crea una clase Autor con atributos nombre y pais.
#• Modifica la clase Libro para que el atributo autor sea un objeto de tipo Autor.
#• En el método mostrar_info(), muestra también el nombre y país del autor

""" class Autor:
     def __init__(self,nombre,pais):
          
         self.nombre = nombre
         self.pais = pais

class Libro:
     
    def __init__(self,titulo,autor,anio_publicacion):
            self.__titulo = titulo
            self.autor = autor
            self.__anio_publicacion = anio_publicacion

    def mostrar_info(self):
        return f"Titulo:{self.__titulo} - Autor:{self.autor.nombre}- Pais:{self.autor.pais} - Año publicacion:{self.__anio_publicacion} "
    
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


 
     
autor1= Autor("Marcela paz","Chile")
libro1 = Libro("Papelucho y el marciano",autor1,1968) 
print(libro1.mostrar_info())
 """






#5. Composición
#• Crea una clase Editorial con atributos nombre y ciudad.
#• Modifica la clase Libro para que tenga un atributo editorial (objeto de tipo Editorial).
#• Asegúrate de que la instancia de Editorial se cree dentro del constructor de Libro

class Editorial: 
     def __init__(self,nombre,ciudad):
          self.nombre = nombre
          self.ciudad = ciudad

class Autor:
     def __init__(self,nombre,pais):
          
         self.nombre = nombre
         self.pais = pais

class Libro:
    
    def __init__(self,titulo,autor,anio_publicacion,nom_edi,ciu_edi):
            self.__titulo = titulo
            self.autor = autor
            self.__anio_publicacion = anio_publicacion
            self.editorial = Editorial(nom_edi,ciu_edi)


    def mostrar_info(self):
        return f"Titulo:{self.__titulo} - Autor:{self.autor.nombre}- Pais:{self.autor.pais} - Año publicacion:{self.__anio_publicacion} - Editorial:{self.editorial.nombre}  "
    
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


 
     
autor1= Autor("Marcela paz","Chile")
libro1 = Libro("Papelucho y el marciano",autor1,1968,"Andres Bello","Santiago") 
print(libro1.mostrar_info())
