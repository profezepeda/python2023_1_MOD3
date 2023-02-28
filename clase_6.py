from librerias.lib_clase6 import Persona, concatenar_listas, crear_persona, describir_diccionario, imprimir_elementos, mostrar, sumar


print("La suma es", sumar(b=2, a=3))
print("La suma es", sumar(b=12, a=31.5))
print("La suma es", sumar(50, 12, 3))

juan: Persona = Persona("Juan", "Perez", 30)
print(juan.nombre_completo())

juan.imprimir_nombre_completo()

crear_persona("María", "González", 30).imprimir_nombre_completo()

jose: Persona = crear_persona(edad=30, apellido="González", nombre="José")
jose.imprimir_nombre_completo()

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

imprimir_elementos(lista1)
imprimir_elementos(lista2)

lista3 = concatenar_listas(lista1, lista2)
imprimir_elementos(lista3)

diccionario = {
  "nombre": "Juan",
  "apellido": "Perez",
  "edad": 30
}
describir_diccionario(diccionario)

mostrar(nombre="Juan", apellido="Perez", edad=30)



def f():
  global ciudad
  # ciudad = "Buenos Aires"
  print("Ciudad 1", ciudad)

ciudad = "Rosario"
f()


