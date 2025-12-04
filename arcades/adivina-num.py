import time
import random

def adivina_numero():
    print("\n--- Adivina el número ---")
    # Genera un número aleatorio entre 1 y 20
    MIN_NUM = 1
    MAX_NUM = 20
    numero = random.randint(MIN_NUM, MAX_NUM)
    intentos = 5
    
    # Mejora: Informa al usuario del rango
    print(f"Estoy pensando en un número entre {MIN_NUM} y {MAX_NUM}.")
    print(f"Tienes {intentos} intentos para adivinarlo.")
    print("-" * 30)

    for i in range(intentos):
        # El número de intento se calcula como i + 1
        entrada = input(f"Intento {i+1}/{intentos}: ")
        
        # Manejo de errores: asegura que la entrada sea un número entero
        try:
            guess = int(entrada)
        except ValueError: # Especificamos el tipo de excepción para ser más exactos
            print("❌ Introduce un número válido (ej. 1, 15, 20).")
            continue # Vuelve al inicio del bucle sin contar este intento fallido
            
        
        # Comprobación de la suposición
        if guess == numero:
            print(f"\n🎉 ¡Correcto! Lo adivinaste en {i+1} intentos.")
            # Añadimos una pausa para simular un juego más pulido
            time.sleep(1) 
            return # Finaliza la función y el juego
        elif guess < numero:
            print("⬆️ Más alto.")
        else: # guess > numero
            print("⬇️ Más bajo.")

        # Pausa ligera para mejor flujo
        time.sleep(0.5)

    # Este código se ejecuta si el bucle termina sin encontrar el número (es decir, se acabaron los intentos)
    print("\n--- ¡Fin del juego! ---")
    print(f"💔 No acertaste. El número secreto era {numero}.")

# 🚨 CORRECCIÓN CLAVE: Llama a la función para que el juego comience al ejecutar el script.
if __name__ == "__main__":
    adivina_numero()