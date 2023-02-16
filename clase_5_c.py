persona = {
  "nombre": "Juan",
  "apellido": "Perez",
  "edad": 25,
  "hobbies": ["futbol", "peliculas", "videojuegos"],
}

# print(persona["nombre"])
# print(persona["apellido"])
# print(persona["edad"])

personas = [
  {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  },
  {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  },
  {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  }
]

# print(personas[0]["hobbies"][0])


personas2 = [
  {
    "nombre": { 
      "primer_nombre": "Juan", 
      "primer_apellido": "Pérez"
    },
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  },
  {
    "nombre": { 
      "primer_nombre": "Juan", 
      "primer_apellido": "Pérez"
    },
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  },
  {
    "nombre": { 
      "primer_nombre": "Juan", 
      "primer_apellido": "Pérez"
    },
    "edad": 25,
    "hobbies": ["futbol", "peliculas", "videojuegos"],
  }
]

# # print(personas2[0]["nombre"]["primer_nombre"])

print(persona)
persona["estatura"] = 1.75
print(persona)
# del persona["estatura"]
persona.pop("estatura")
print(persona)


for key in persona.keys():
  print(key, persona[key])

print(len(persona))
print(min(persona))
print(max(persona))

# for value in persona.values():
#   print(value)
