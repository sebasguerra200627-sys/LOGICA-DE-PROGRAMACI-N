import random # Obligatorio para elegir letras

# 1. Mensaje de bienvenida
print("Bienvenido al generador de contraseñas")

# 2. Pedir datos al usuario (usamos un bucle while por si pone un número menor a 8)
longitud = 0
while longitud < 8:
    longitud = int(input("Escribe el tamaño de tu contraseña (mínimo 8): "))
    # Condicional para mostrar error
    if longitud < 8:
        print("Error: la contraseña debe tener al menos 8 caracteres.")

quiere_numeros = input("¿Quieres usar números? (si/no): ")
quiere_simbolos = input("¿Quieres usar símbolos? (si/no): ")

# 3. Guardar las letras que vamos a usar
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+"

# Juntamos las opciones según lo que dijo el usuario
opciones = letras

# Condicionales simples
if quiere_numeros == "si":
    opciones = opciones + numeros

if quiere_simbolos == "si":
    opciones = opciones + simbolos

# 4. Generar la contraseña usando un bucle for
contrasena_final = ""

for i in range(longitud):
    letra_al_azar = random.choice(opciones)
    contrasena_final = contrasena_final + letra_al_azar

# 5. Mostrar el resultado
print("Tu contraseña segura es:", contrasena_final)