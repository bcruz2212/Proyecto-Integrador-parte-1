# Pedir el nombre del jugador por teclado
#Imprimir un mensaje de bienvenida con el nombre


print("Bienvenido al juego, cual es tu nombre?:")
nombre = input()
print("Tu nombre es: ", nombre)

#Parte2:
import readchar
while True:
    keypress = readchar.readkey()
    if keypress == readchar.key.UP:
        break
    print(keypress)
