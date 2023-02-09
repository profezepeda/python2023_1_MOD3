from datetime import datetime, date

print("String to int", int("123"))
print("String to float", float("123.456"))
print("String to bool", bool("True"))
print("String to hex", hex(123))
print("String to oct", oct(123))
print("Tupla to list", list((1, 2, 3)))
print("List to tupla", tuple([1, 2, 3]))

print("String", str(123))

fecha_hora = "Hoy es " + str(date.today())
print(fecha_hora)

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print(datetime.now().year)

# print(dir(datetime))

# IF, ELSE, ELIF

edad = 62
sexo = "M"

if (sexo == "M" and edad >= 60) or (sexo == "H" and edad >= 65):
  print("Es adulto mayor")
elif edad >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")

for contador in range(8, 10):
  print(contador)

valor1 = 20
valor2 = 10
while valor2 <= valor1:
  print(valor2)
  valor2 += 1
