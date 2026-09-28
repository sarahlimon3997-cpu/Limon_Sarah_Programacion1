# ==========================================
# Unidad 2 - Práctica 2.1
# ==========================================

# Ejercicio 1: Datos personales
nombre, edad, ciudad = "Sarah", 18, "Guadalajara"
print(nombre, edad, ciudad)

# Ejercicio 2: Actualizar un contador
contador = 0
contador += 1; print(contador)
contador += 1; print(contador)
contador += 1; print(contador)

# Ejercicio 3: Constante de conversión
PULGADAS_A_CM = 2.54
pulgadas = 10
print("Prueba 1:", pulgadas * PULGADAS_A_CM, "cm")
pulgadas = 5
print("Prueba 2:", pulgadas * PULGADAS_A_CM, "cm")

# Ejercicio 4: Área de un rectángulo
base, altura = 10, 4.5
area = base * altura
print("El área es:", area)
perimetro = 2 * (base + altura)
print("El perímetro es:", perimetro)

# Ejercicio 5: Total con IVA
IVA = 0.16
precio = 200
print("Total 1:", precio + (precio * IVA))
precio = 500
print("Total 2:", precio + (precio * IVA))

# Ejercicio 6: Intercambio de valores
a, b = 10, 20
print("Antes:", a, b)
temp = a
a, b = b, temp
print("Después:", a, b)
a, b = b, a  # Extra abreviado

# Ejercicio 7: Identificar tipos con type()
entero, decimal, texto, booleano = 25, 10.5, "Hola", True
print(type(entero))
print(type(decimal))
print(type(texto))
print(type(booleano))

# Ejercicio 8: Convertir tipos
num_int = int("25")
print(num_int, type(num_int))
num_str = str(100)
print(num_str, type(num_str))

# Ejercicio 9: Booleanos y comparaciones
a, b = 8, 3
mayor = a > b
print(mayor)
print(type(mayor))
