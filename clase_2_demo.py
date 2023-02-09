lista = []
while len(lista) < 1:
  articulo = input("Ingrese un artículo: ")
  if articulo == "":
    print("El artículo no puede estar vacío")
    continue
  cantidad = input("Ingrese la cantidad: ")
  if cantidad == "":
    print("La cantidad no puede estar vacía")
    continue
  if not cantidad.isnumeric():
    print("La cantidad debe ser un número")
    continue
  lista.append({"articulo": articulo, "cantidad": cantidad})

print(lista)



