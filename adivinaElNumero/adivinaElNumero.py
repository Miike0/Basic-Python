import random

def main():
    vidas = 10
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un número del 1-100: "))
    while numero_elegido != numero_aleatorio and vidas > 0:
        if numero_elegido < numero_aleatorio:
            print("Busca un número mas grande")
        else:
            print("Busca un número mas pequeño")
        vidas-=1
        numero_elegido = int(input("Elige otro número: "))
    if vidas > 0:
        print("Ganaste!")
    else:
        print("Perdiste!")

if __name__ == '__main__':
    main()