import time
import random

def calculo_mental():
    print("\n--- Cálculo mental ---")
    print("Tienes 20 segundos. Responde lo máximo posible.")
    aciertos = 0
    
    # ⏱️ Se registra el tiempo de inicio
    inicio = time.time()

    while time.time() - inicio < 20:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-", "*"])

        if op == "+":
            correcto = a + b
        elif op == "-":
            correcto = a - b
        else:
            correcto = a * b

        # ❗ Aquí está el problema: si el usuario tarda mucho en escribir, el tiempo sigue corriendo.
        entrada = input(f"{a} {op} {b} = ")
        
        # 💡 MEJORA: Puedes verificar si ya se acabó el tiempo después de la entrada
        if time.time() - inicio >= 20:
            print("\n¡Se acabó el tiempo mientras escribías!")
            break


        try:
            respuesta = int(entrada)
        except ValueError: # Especificamos el error para ser más precisos
            print("Número inválido.")
            continue

        if respuesta == correcto:
            aciertos += 1
            print("¡Correcto!")
        else:
            print(f"Incorrecto, era {correcto}.")
        
        # Se añade una pequeña pausa para un mejor flujo
        time.sleep(0.1)

    print(f"\nTiempo acabado. Aciertos: {aciertos}")

# 🚨 CORRECCIÓN CLAVE: Llama a la función para que se ejecute el juego.
if __name__ == "__main__":
    calculo_mental()