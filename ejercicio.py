import random

character = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de la contraseña: "))

contrasena = ""

for i in range(longitud):
    contrasena += random.choice(character)

print("Contraseña generada:", contrasena)
