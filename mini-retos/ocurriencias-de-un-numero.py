nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

buscar = 6
contador = 0
for n in nums:
    if n == buscar:
        contador += 1

print(f"{buscar} aparece {contador} veces")   # 3 veces