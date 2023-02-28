
class Persona():
  nombre: str
  apellido: str
  edad: int

  def __init__(self, nombre: str = '', apellido: str = '', edad: int = 0) -> None:
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def nombre_completo(self) -> str:
    return f'{self.nombre} {self.apellido}'

  def imprimir_nombre_completo(self) -> None:
    print(self.nombre_completo())


def sumar(a: int, b: int, c: int = 0) -> int:
  resulado = a + b + c
  return resulado

def crear_persona(nombre: str, apellido: str, edad: int) -> Persona:
  return Persona(nombre, apellido, edad)

def imprimir_elementos(lista: list) -> None:
  for elemento in lista:
    print(elemento)

def concatenar_listas(lista1: list, lista2: list) -> list:
  return lista1 + lista2

def describir_diccionario(diccionario: dict) -> None:
  for clave, valor in diccionario.items():
    print(f'La clave es {clave} y el valor es {valor}')

def mostrar(**parametros):
  describir_diccionario(parametros)
