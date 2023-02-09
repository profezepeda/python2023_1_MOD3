productos = [
  { "sku": "123", "nombre": "Producto 1", "precio": 1000 },
  { "sku": "456", "nombre": "Producto 2", "precio": 2000 },
  { "sku": "789", "nombre": "Producto 3", "precio": 3000 },
  { "sku": "101", "nombre": "Producto 4", "precio": 4000 },
  { "sku": "112", "nombre": "Producto 5", "precio": 5000 }
]

for producto in productos:
  print(producto["sku"], producto["nombre"], producto["precio"])
  cantidad = input("Ingrese la cantidad: ")
  while not cantidad.isnumeric():
    print("La cantidad debe ser un número")
    cantidad = input("Ingrese la cantidad: ")
  producto["cantidad"] = int(cantidad)
  producto["total"] = producto["precio"] * producto["cantidad"]

suma = 0
for producto in productos:
  suma += producto["total"]
  print(producto["sku"], producto["nombre"], producto["precio"], producto["cantidad"], producto["total"])

iva = int(suma * 0.19)
print("NETO: ", suma)
print("IVA: ", iva)
print("TOTAL: ", suma + iva)