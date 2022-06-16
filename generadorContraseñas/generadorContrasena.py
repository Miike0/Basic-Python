from ctypes.wintypes import CHAR
import random

def generar_contrasenia():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
             'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', 
             ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres = MAYUS + MINUS + NUMS + CHARS
    
    contrasenia = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasenia.append(caracter_random)
        
    contrasenia = "".join(contrasenia)
    return contrasenia

def main():
    contasenia = generar_contrasenia()
    print("Tu nuevo contaseña es: " +  contasenia)


if __name__ == '__main__':
    main()