

class Persona:
   
    def __init__(self,rut,nombre,apellido,tipo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
       
    def mostrar_datos(self):#poliformismo
         return (f"Rut:{self.rut}\n"
              f"nombre:{self.nombre}\n"
              f"Apellido:{self.apellido}\n"
              f"Tipo:{self.tipo}\n")
        

    
class Alumno(Persona): #hereda de la clase persona
   def __init__(self,persona):
      super().__init__(persona.rut,persona.nombre,persona.apellido,persona.tipo)

   def mostrar_datos(self):#poliformismo
         return (f"Rut:{self.rut}\n"
              f"nombre:{self.nombre}\n"
              f"Apellido:{self.apellido}\n")
             

      
   
class Profesor(Persona): #hereda de la clase persona
    def __init__(self,persona,especialidad):
      super().__init__(persona.rut,persona.nombre,persona.apellido,persona.tipo)
      self.especialidad = especialidad
      self.curso_cargo = None
   
    def mostrar_datos(self):#poliformismo
         if self.curso_cargo:
            nombre_del_curso = self.curso_cargo.nom_curso
         else:
            nombre_del_curso = "Sin curso asignado"
         return (f"Rut:{self.rut}\n"
              f"nombre:{self.nombre}\n"
              f"Apellido:{self.apellido}\n"
              f"Especialidad:{self.especialidad}\n"
              f"Curso a cargo:{nombre_del_curso}")   



class Curso:
   def __init__(self,cod_curso,nom_curso):
      self.cod_curso = cod_curso
      self.nom_curso = nom_curso
      self.profesor_jefe = None
      self.asignatura_curso = []
      self.alumnos_matriculados = []




   def mostrar_info(self):
      nombres_asignaturas = ""
      for asig in self.asignatura_curso:
            nombres_asignaturas += f"{asig.nombre}, "
      return (f"Codigo del curso:{self.cod_curso}\n"
              f"Nombre curso:{self.nom_curso}\n"
              f"Profesor jefe:{self.profesor_jefe.nombre}\n"
              f"Asignaturas:{nombres_asignaturas}\n"
              f"Cantidad de alumnos:{len(self.alumnos_matriculados)}")
   

   def agregar_alumno(self, nuevo_alumno):
        self.alumnos_matriculados.append(nuevo_alumno)

   def agregar_asignatura(self, nueva_asignatura):
        self.asignatura_curso.append(nueva_asignatura)  

   def asignar_profesor(self, nuevo_profesor):
         self.profesor_jefe = nuevo_profesor
         nuevo_profesor.curso_cargo = self  

class Asignatura: 
   def __init__(self,cod_asignatura,nombre):
      self.cod_asignatura = cod_asignatura
      self.nombre = nombre
      

persona1= Persona("16551814-4","Andres","Moraga","Alumno")
persona2= Persona("11551614-4","Monica","Escobar","Alumno")
persona3= Persona("15814478-5","roberto","cox","profesor")
persona4= Persona("8565789-4","Angelica","Gallardo","Auxiliar")
persona5= Persona("10478956-7","Marta","Loncomilla","profesor")
alumno1= Alumno(persona1)
alumno2= Alumno(persona2)
profesor1= Profesor(persona3,"Lenguaje")
profesor2= Profesor(persona5,"Lenguaje")
asignatura1= Asignatura(1,"Lenguaje")
asignatura2= Asignatura(2,"Matematicas")
asignatura3= Asignatura(3,"Musica")
curso1= Curso(1,"1° basico")
curso1.agregar_alumno(alumno1)
curso1.agregar_alumno(alumno2)
curso1.agregar_asignatura(asignatura1)
curso1.agregar_asignatura(asignatura2)
curso1.agregar_asignatura(asignatura3)
curso1.asignar_profesor(profesor2)


print(alumno1.mostrar_datos())
print("__________________________")
print(alumno2.mostrar_datos()) 
print("__________________________")
print(profesor2.mostrar_datos())
print("__________________________")
print(profesor1.mostrar_datos())
print("__________________________")
print(curso1.mostrar_info())
