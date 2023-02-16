meses = [
  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]
primer_semestre = meses[1:6]
print(primer_semestre)
segundo_semestre = meses[-6:-3]
print(segundo_semestre)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print(len(numeros) + len(numeros2))

numeros_resultado = numeros + numeros2 + meses
ejemplo_mes = meses[0] + " " + meses[1]
print(ejemplo_mes)
print(numeros)
print(numeros2)
print(numeros_resultado)

valores = [10, "ab"] * 10
print(valores)

print("Diciembre" in meses)
# print(input("Ingrese un mes:") in meses)

for mes in meses:
  print(mes)


# usuarios = [
#   ["juan", "1234"],
#   ["maria", "1234"],
#   ["pedro", "1234"]
# ]

# usuarios[1][1] = "catalina"
# usuarios[0][1] = "colocolo"

# while True:
#   usuario = input("Ingrese su usuario: ")
#   password = input("Ingrese su contraseña: ")
#   if [usuario, password] in usuarios:
#     print("Usuario válido")
#     break
#   else:
#     print("Usuario no válido")

# while True:
#   usuario = input("Ingrese su usuario: ")
#   password = input("Ingrese su contraseña: ")
  # usuario_valido = False
  # for user in usuarios:
  #   if user == [usuario,password]:
  #     print("Usuario válido")
  #     usuario_valido = True
  #     break
  # if usuario_valido:
  #   break
  # else:
  #   print("Usuario o contraseña incorrecta")

print(len(numeros))
print(min(numeros))
print(max(numeros))

print(numeros)
del numeros[1:3]
numeros.append(21)
numeros[-1] = "veintiuno"
print(numeros)
# numeros.clear()
# print(numeros)
n = numeros.copy()
print(n)

print(numeros.index(12))
numeros.insert(10, 30)
print(numeros)
numeros.pop(10)
print(numeros)
numeros.remove("veintiuno")
print(numeros)
numeros.reverse()
print(numeros)
# meses.reverse()
# print(meses)
# meses.sort()
# print(meses)

tmeses = tuple(meses)
print(tmeses)
print(tmeses[0])
for mes in tmeses:
  print(mes)
print("Diciembre" in tmeses)
print(len(tmeses))
print(min(tmeses))
print(max(tmeses))



