import time, random

productos = [
  { "nombre": "Producto 1", "saldo": 120},
  { "nombre": "Producto 2", "saldo": 150},
]
proveedores = [0, 0]

contador = 0
while True:
  time.sleep(3)
  indice_producto = random.randint(0, len(productos)-1)
  cantidad = random.randint(1,10)
  if productos[indice_producto]["saldo"] < cantidad:
    cantidad = productos[indice_producto]["saldo"]
  productos[indice_producto]["saldo"] -= cantidad
  contador += 1
  if contador == 10:
    saldo_total = 0
    for producto in productos:
      print(producto["nombre"], "tiene un saldo de ...", producto["saldo"])
      print("El proveedor ha suministrado ...", proveedores[productos.index(producto)])
      saldo_total += producto["saldo"]
    if saldo_total == 0:
      print("No hay más productos")
      break
    contador = 0
  if productos[indice_producto]["saldo"] < 100 and proveedores[indice_producto] < 150:
    productos[indice_producto]["saldo"] += 50
    proveedores[indice_producto] += 50
