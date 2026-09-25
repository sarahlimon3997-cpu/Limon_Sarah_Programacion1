import time


def decir(personaje, texto, espera=2):
    print(f"{personaje}: {texto}")
    time.sleep(espera)

# --- SECUENCIA DE SCRATCH ---
print("--- FONDO: PISCINA ---")
decir("Perro", "hola chikos bienvenidos a mi piscina gg")

print("\n[Aparece el personaje 'Random']")
decir("Perro", "noooo y este random?")
decir("Random", "hola soy un random ajjajashjas lol")
decir("Perro", "noo no me la creo entro un random a mi casa")
decir("Perro (pensando)", "no se q hacer chavales")

# Pregunta interactiva
respuesta = input("\nPerro pregunta: que tengo q hacer o q? -> ")
print(f"[Variable guardada: {respuesta}]\n")

decir("Perro (pensando)", "no se pq pregunte igual le voy a pegar")
def new_func(decir):
    decir("Perro", "manos a la obra")

new_func(decir)

print("\n--- FONDO: PARED DE LADRILLO CON CESPED ---")
decir("Random", "que", 1)
decir("Perro", "te voi yaser pikadillo")

print("\n[El Perro se mueve hacia el Random y lo derriba]")
decir("Perro", "andele", 1)