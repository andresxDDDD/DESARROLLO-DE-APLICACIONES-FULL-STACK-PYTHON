#¿Qué es la programación orientada a objetos?

#La Programación Orientada a Objetos (POO) es un paradigma de programación, es decir, 
# una forma de organizar el código, que se basa en la idea de que los programas deben 
# estructurarse en torno a "objetos" en lugar de solo funciones o lógica pura.


#¿En qué se diferencia de la programación estructurada?

#La principal diferencia radica en el enfoque. Mientras que la programación estructurada
#  se centra en el "cómo" (los pasos a seguir), la programación orientada a objetos (POO)
#  se centra en el "quién" (los actores o componentes que interactúan)

#Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto.

# un ejemplo podria ser el smartphone. que puede ser un objeto abstraido de una clase padre 
# telefono. tiene sus atributos como "marca, bateria, almacenamiento" y metodos como "hacer llamada"
#o tomar foto"


#Diferenciar conceptos Clase, instancia y objeto

# CLASE: Es el plano, el molde o la definición. No existe físicamente en la memoria.
# OBJETO: Es la entidad conceptual que nace de la clase. 
# INSTANCIA: Es el objeto real que ocupa un lugar en la memoria.
# La Clase es el diseño del auto; el Objeto es el auto fabricado; 
# la Instancia es ese auto en tu casa listo para ser usado. 

#Diferenciar conceptos Atributo y estado

#El Atributo es el "campo" ejemplo bateria; el Estado es el "valor" 
# de ese campo en este segundo ejemplo batateria descargada.

#Diferenciar Método y comportamiento

#COMPORTAMIENTO: Es la respuesta visible del objeto cuando se ejecuta un método.
# Es lo que sucede cuando el objeto interactúa con el mundo.
#El Método es la instrucción programada; el Comportamiento es la acción o reacción
#  que el objeto manifiesta al ejecutar esa instrucción.

#Definición de una clase simple
# Crea una clase llamada Perro.
# Agrega atributos como nombre, edad y raza.
# Define un método ladrar() que imprima "¡Guau!".
# Crea una instancia de la clase Perro y llama al método ladrar().

""" class Perro():
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza 
        pass
    def ladrar(self): 
        print(f"{self.nombre} el perro hace guauuu")

perro1 = Perro("terry",12,"kiltro")
perro1.ladrar() """


#Principios de POO
# Modifica la clase Perro para que los atributos estén encapsulados (prefijo _).
# Agrega un método mostrar_info() que devuelva el estado del objeto en forma de texto.



class Perro():
    def __init__(self,nombre,edad,raza):
        self.__nombre = nombre
        self.__edad = edad
        self.__raza= raza 
        pass
    def ladrar(self): 
        print(f"{self.nombre} el perro hace guauuu")

    def mostrar_info(self):
       print(f"El perro se llama:{self.__nombre} es de raza:{self.__raza} y tiene: {self.__edad} años")


perro1 = Perro("terry",12,"kiltro")
perro1.mostrar_info()

# Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo

#La Abstracción es el proceso de simplificar la realidad para quedarnos solo con lo que
#  es importante. en este ejemplo abstraimos en la clase a un perro que es de nuestra realidad 
# describiendo atributos y metodos.  