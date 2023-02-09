# String

primer_nombre = "Juan"
segundo_nombre = "Pablo"
primer_apellido = "Gomez"
segundo_apellido = "Perez"
nombre_completo = primer_nombre + " " + segundo_nombre + " " + primer_apellido + " " + segundo_apellido

print(nombre_completo)
print(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)

print("María" in nombre_completo)

nombre_completo = nombre_completo.replace("Perez", "Pérez")
print(nombre_completo.upper())
print(nombre_completo.lower().capitalize())

print(",".join(primer_nombre))
print(nombre_completo.split(" "))

print(primer_nombre[0])
print(primer_nombre[0:3])
print(primer_nombre[2:])


# TUPLAS
# tuplas

mi_tupla = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
print(mi_tupla)
print(mi_tupla[2])

mi_tupla = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(mi_tupla)

tupla_2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_2)
print(tupla_2[0][1])


for elemento in mi_tupla:
    print(elemento)

for elemento in tupla_2:
    print(elemento)
    for subelemento in elemento:
      print(subelemento)

# LISTAS
mi_lista = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]
print(mi_lista)

mi_lista.append(89)
print(mi_lista)
del mi_lista[11]
print(mi_lista)

for numero in mi_lista:
    print(numero)

del mi_lista[2]
print(mi_lista)
mi_lista.insert(2, 1)
print(mi_lista)

print("7 es fibonnaci? ", 7 in mi_lista)
print("largo", len(mi_lista))
tupla_fibonnaci = tuple(mi_lista)
print(tupla_fibonnaci)

# lista desordenada
mi_lista_desordenada = [ 3, 1, 2, 5, 4 ]
print(mi_lista_desordenada)
print(sorted(mi_lista_desordenada, reverse=True))
print(mi_lista_desordenada)

mi_lista_desordenada.sort()
print(mi_lista_desordenada)

# lista de strings desordenada con 4 caracters
mi_lista_strings = [ "casa", "auto", "perro", "gato", "amigo", "armadillo" ]
print(mi_lista_strings)
print(sorted(mi_lista_strings))

# tablero de ajedez con listas
tablero = [ ["torre", "caballo", "alfil", "rey", "reina", "alfil", "caballo", "torre"],
            ["peon", "peon", "peon", "peon", "peon", "peon", "peon", "peon"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["peon", "peon", "peon", "peon", "peon", "peon", "peon", "peon"],
            ["torre", "caballo", "alfil", "rey", "reina", "alfil", "caballo", "torre"] ]

for fila in tablero:
    for columna in fila:
        print(columna, end=" ")
    print()
