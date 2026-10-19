 Alumno: Sarah Michelle Limon Illan
# Mini proyecto: U2 - Recibo de compra interactivo

# Captura y validacion de la cantidad de productos
while True:
    cantidad_str = input("¿Cuántos productos vas a registrar?: ")
    if cantidad_str.isdigit() and int(cantidad_str) > 0:
        num_productos = int(cantidad_str)
        break
    print("Error: Ingresa un número entero mayor que cero.")

# Preparar listas para guardar los datos de cada producto
productos = []
precios = []
cantidades = []
subtotales = []

# Captura y validacion de los datos de cada producto
for i in range(num_productos):
    print(f"\nProducto {i + 1}:")

    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede quedar vacío.")

    while True:
        precio_str = input("Precio unitario: $").strip()
        try:
            precio = Decimal(precio_str)
            if not precio.is_finite() or precio < 0:
                raise InvalidOperation
            precio = precio.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            break
        except InvalidOperation:
            print("Error: Ingresa un precio válido, por ejemplo 25.50.")

    while True:
        cantidad_str = input("Cantidad de unidades: ").strip()
        if cantidad_str.isdigit() and int(cantidad_str) > 0:
            cantidad = int(cantidad_str)
            break
        print("Error: Ingresa una cantidad entera mayor que cero.")

    # Calcular y guardar el subtotal de este producto
    subtotal_producto = precio * cantidad
    productos.append(nombre)
    precios.append(precio)
    cantidades.append(cantidad)
    subtotales.append(subtotal_producto)

# Calculo del subtotal de la compra, IVA y total a pagar
subtotal_compra = sum(subtotales, Decimal("0.00"))
iva = (subtotal_compra * Decimal("0.16")).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)
total_pagar = subtotal_compra + iva

# Impresion del recibo con todos los montos en formato de dos decimales
print("\n" + "=" * 58)
print("                     RECIBO DE COMPRA")
print("=" * 58)
print(f"{'Producto':<22}{'Precio':>11}{'Cant.':>7}{'Subtotal':>14}")
print("-" * 58)

for i in range(num_productos):
    print(
        f"{productos[i]:<22}"
        f"${precios[i]:>10.2f}"
        f"{cantidades[i]:>7}"
        f"${subtotales[i]:>13.2f}"
    )

print("-" * 58)
print(f"{'Subtotal de la compra:':>44} ${subtotal_compra:>10.2f}")
print(f"{'IVA (16%):':>44} ${iva:>10.2f}")
print(f"{'TOTAL A PAGAR:':>44} ${total_pagar:>10.2f}")
print("=" * 58)
