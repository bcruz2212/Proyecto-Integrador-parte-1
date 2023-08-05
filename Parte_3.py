#Parte3: 
import os
import readchar
#Limpiar pantalla
os.system('cls' if os.name=='nt' else 'clear')
numero=0
print(numero)

#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
def clear(n):
    os.system('cls' if os.name=='nt' else 'clear')
    print(n)

while True:
    t=readchar.readkey()
    if t == 'n' or t == 'N':
        numero +=1
        clear(numero)
        if numero == 50:
            break
