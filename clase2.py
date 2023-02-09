persona = {
  "primer_nombre": "Juan",
  "segundo_nombre": "Pablo",
  "primer_apellido": "Gomez",
  "segundo_apellido": "Perez",
  "edad": 30,
  "hijos": [ "Maria", "Pedro", "Jose" ]
}
persona2 = {
  "primer_nombre": "Maria",
  "segundo_nombre": "Jose",
  "primer_apellido": "Gomez",
  "segundo_apellido": "Perez",
  "edad": 30,
  "hijos": [ "Maria", "Pedro", "Jose" ]
}

meses = {
  "ene": "Enero",
  "feb": "Febrero",
  "mar": "Marzo",
  "abr": "Abril",
  "may": "Mayo",
  "jun": "Junio",
  "jul": "Julio",
  "ago": "Agosto",
  "sep": "Septiembre",
  "oct": "Octubre",
  "nov": "Noviembre",
  "dic": "Diciembre"
}

print(meses["sep"])
print(persona["primer_nombre"] + " " + persona["primer_apellido"])

mis_personas = []
mis_personas.append(persona)
mis_personas.append(persona2)

print(mis_personas[0]["primer_nombre"])

print(persona["primer_nombre"])


for elemento in persona.keys():
  print(elemento, persona[elemento])

for elemento in persona.values():
  print(elemento)

for key,value in persona.items():
  print(key, value)

# del persona["edad"]
# print(persona)

procesado = sorted(persona)
print(procesado)
persona_to_send = {}
for elemento in procesado:
  persona_to_send[elemento] = persona[elemento]
print(persona)
print(persona_to_send)


# código para generar la serie fibonacci en python
serie = []
for i in range(0, 20):
  if i == 0:
    serie.append(0)
  elif i == 1:
    serie.append(1)
  else:
    serie.append(serie[i-1] + serie[i-2])

print(serie)



for elemento in range(0,5):
  print(elemento)