pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}
letras = set("string")
numeros = set(range(1, 101))


print("s" in letras)

pares.add(12)
for par in pares:
  print(par)
respaldo_numeros = numeros.copy()
# numeros.clear()
pares.pop()
print(pares)

print(pares.union(impares))
print("intersección", numeros.intersection(impares))
print("diferencia", numeros.difference(impares))

impares.update({11, 13, 15, 17, 19})
print(impares)
pares.discard(12)
print(pares)
