def eco_loco():
    print("\n--- Eco loco ---")
    print("Escribe texto. Enter vacío para salir.\n")

    while True:
        txt = input("Texto: ")

        if txt == "":
            print("Volviendo al menú...")
            return

        invertido = txt[::-1]
        vocales = sum(1 for c in txt.lower() if c in "aeiouáéíóúü")

        print(f"Invertido: {invertido}")
        print(f"Caracteres: {len(txt)} | Vocales: {vocales}")
