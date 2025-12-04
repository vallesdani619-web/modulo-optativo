import random

print("Bienvenido al juego: Piedra, Papel o Tijera")

opciones = ["Piedra","Papel","Tijera"]
user_pts = 0
machine_pts = 0
fin = False

while not fin:
    eleccion = int(input("1-Piedra\n2-Papel\n3-Tijera\Elige una opción:(1,2,3):"))
    bot = random.randint(1,3)
    print(f"Tu: {opciones[eleccion-1]} | Bot: {opciones[bot-1]}")
    if eleccion == bot:
        print("¡Empate!")
    elif (eleccion==1 and bot==3) or (eleccion==2 and bot==1) or (eleccion==3 and bot==2):
        print("¡Ganaste!")
        
    else:
        print("¡Perdiste!")
        machine_pts +=1
    
    if user_pts==3 or machine_pts==3:
        fin = True
        
if user_pts==3:
    print("¡Has ganado el juego!")
else:
    print("¡Has perdido el juego!")
    