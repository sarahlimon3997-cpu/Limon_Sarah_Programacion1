# ==========================================
# Práctica 2.1: Tipos de datos básicos en Python
# Nombre: Sarah Michelle Limón Illan
# Edad: 19 años
# Ciudad: Guadalajara
# ==========================================

# Ejercicio 1: Datos personales
nombre = "Sarah Michelle"
edad = 19
ciudad = "Guadalajara"

print(nombre, edad, ciudad)


# Ejercicio 2: Actualizar un contador
contador = 0

contador = contador + 1
print(contador)

contador = contador + 1
print(contador)

contador = contador + 1
print(contador)


# Ejercicio 3: Constante de conversión
PULGADAS_A_CM = 2.54
pulgadas = 10

centimetros = pulgadas * PULGADAS_A_CM
print(centimetros)


# Ejercicio 4: Área de un rectángulo
base = 9
altura = 5

area = base * altura
perimetro = 2 * (base + altura)

print("El área es:", area)
print("El perímetro es:", perimetro)


# Ejercicio 5: Total con IVA
IVA = 0.16
precio = 200

total = precio + (precio * IVA)
print("El total a pagar es:", total)


# Ejercicio 6: Intercambio de valores
a = 10
b = 20

print("Antes del intercambio:")
print("a =", a)
print("b =", b)

# Intercambio usando variable auxiliar
temp = a
a = b
b = temp

print("Después del intercambio:")
print("a =", a)
print("b =", b)

# Forma abreviada en Python (Extra):
# a, b = b, a


# Ejercicio 7: Identificar tipos con type()
entero = 19
decimal = 2.54
texto = "Guadalajara"
booleano = True

print(type(entero))
print(type(decimal))
print(type(texto))
print(type(booleano))


# Ejercicio 8: Convertir tipos
texto_numero = "25"
numero_convertido = int(texto_numero)
print(numero_convertido, type(numero_convertido))

numero_entero = 100
texto_convertido = str(numero_entero)
print(texto_convertido, type(texto_convertido))


# Ejercicio 9: Booleanos y comparaciones
num_a = 8
num_b = 3

mayor = num_a > num_b

print("Resultado de la comparación:", mayor)
print("Tipo de dato:", type(mayor))
