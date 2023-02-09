from datetime import date

class Personas:
  primer_nombre: str
  segundo_nombre: str
  primer_apellido: str
  segundo_apellido: str
  fecha_nacimiento: date

  def __init__(self, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento):
    self.primer_nombre = primer_nombre
    self.segundo_nombre = segundo_nombre
    self.primer_apellido = primer_apellido
    self.segundo_apellido = segundo_apellido
    self.fecha_nacimiento = fecha_nacimiento

  def __str__(self):
    return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido} {self.fecha_nacimiento}"

  def saludar(self):
    print("Hola " + self.primer_nombre)

juan: Personas = Personas("Juan", "Pablo", "Gonzalez", "Gonzalez", date(1990, 1, 1))

personas = []
persona: Personas = Personas("Juan", "Pablo", "Gonzalez", "Gonzalez", date(1990, 1, 1))
personas.append(persona)
persona: Personas = Personas("Maria", "Jose", "Gonzalez", "Gonzalez", date(1990, 1, 1))
personas.append(persona)
persona: Personas = Personas("Pedro", "Pablo", "Gonzalez", "Gonzalez", date(1990, 1, 1))
personas.append(persona)

for persona in personas:
  print(persona)
  persona.saludar()
