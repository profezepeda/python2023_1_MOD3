# while input("¿Cómo está el clima? ") == "soleado":
#   print("Toldo abierto")
# print("Toldo cerrado")

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
  print(numero)

posicion = 0
while posicion < len(numeros):
  print(numeros[posicion])
  posicion += 1

for numero in range(1, 11):
  print(numero)

otra_lista = [1, 2, 3, 4, 5, "a", "b", "c", 6, 7, 8, 9, 10]
suma = 0
contar_letras = 0
for elemento in otra_lista:
  if type(elemento) == int:
    suma += elemento
  else:
    contar_letras += 1
print("Suma: ", suma)
print("Letras: ", contar_letras)

"""

# while True: print("Hola")

personas = [
  {
    "nombre": "Juan",
    "edad": 20
  },
  {
    "nombre": "Pedro",
    "edad": 30
  },
  {
    "nombre": "Maria",
    "edad": 25
  },
  {
    "nombre": "Jose",
    "edad": 40
  }
]

def decir_hola(persona):
  pass

for persona in personas:
  if persona["edad"] >= 30:
    #break
    #continue
    pass
  print(persona["nombre"], persona["edad"])

