

class Persona:
    def __init__(self,rut,nombre,apellido):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def ingresar_persona(self):

     pass

    
             


class Alumno(Persona):
   def __init__(self, rut, nombre, apellido,tipo):
      super().__init__(rut, nombre, apellido)
      self.tipo = tipo

   def mostrar(self):
      return (f"Rut:{self.rut}\n"
              f"nombre:{self.nombre}\n"
              f"Apellido:{self.apellido}\n"
              f"Tipo:{self.tipo}\n")
        
   
class Profesor(Persona):
   def __init__(self, rut, nombre, apellido,tipo):
      super().__init__(rut, nombre, apellido)
      self.tipo = tipo

   def mostrar(self):
      return (f"Rut:{self.rut}\n"
              f"nombre:{self.nombre}\n"
              f"Apellido:{self.apellido}\n"
              f"Tipo:{self.tipo}\n")



class Curso:
   def __init__(self,cod_curso,nom_curso,profesor_jefe,asignatura):
      self.cod_curso = cod_curso
      self.nom_curso = nom_curso
      self.profesor_jefe = profesor_jefe
      self.asignatura = asignatura


   def mostrar(self):
      return (f"Codigo del curso:{self.cod_curso}\n"
              f"Nombre curso:{self.nom_curso}\n"
              f"Profesor jefe:{self.profesor_jefe}\n"
              f"Asignaturas:{self.asignatura.nombre}\n")


class Asignatura: 
   def __init__(self,cod_asignatura,nombre):
      self.cod_asignatura = cod_asignatura
      self.nombre = nombre
      


asignatura1= Asignatura(1,"Lenjuaje")
curso1= Curso(1,"1° basico","roberto",asignatura1)
Alumno1= Alumno("16551814-4","andres","moraga","alumno")
profesor1= Profesor("15814-478-5","roberto","cox","profesor")
print(Alumno1.mostrar())
print(profesor1.mostrar())
print(curso1.mostrar())