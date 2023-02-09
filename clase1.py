import librerias.valores as valores
from datetime import datetime, date

mi_nombre = "Marcelo" # pon tu nombre
print("hola", mi_nombre)
# mi primer comentario

"""
Este es un comentario más grande.
Puede tener varias líneas.
"""

primer_valor = 10
segundo_valor = 22
print("suma ", primer_valor + segundo_valor)
print("resta ", primer_valor - segundo_valor)
print("multiplicacion ", primer_valor * segundo_valor)
print("division ", primer_valor / segundo_valor)
print("division entera ", primer_valor // segundo_valor)
print("elevado", primer_valor ** segundo_valor)

print(mi_nombre, mi_nombre.upper())

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
  """ Éste ciclo recorre la lista de números """
  if numero % 2 == 0:
    print("par", numero)
  else:
    print("impar", numero)

print("Pi es", valores.PI)
print("suma a+b", valores.suma(2, 3))
print("hoy es", date.today())

print(dir(mi_nombre))
print(mi_nombre.count("a"))