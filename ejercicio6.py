print("introduce tu edad")
edad=int(input())
if edad < 0 or edad > 120:
    print("edad incorrecta")
elif edad < 18:
    print("el alumno es menor de edad ")
else:
    print("el alumno es mayor de edad")