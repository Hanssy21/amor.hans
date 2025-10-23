# -*- coding: utf-8 -*-
import os
import time

def print_heart(text):
    red = "\033[31m"   # código ANSI para rojo
    reset = "\033[0m"  # reset de color
    idx = 0
    length = len(text)
    
    for y in range(15, -15, -1):
        row = ""
        for x in range(-30, 30):
            formula = ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3
            if formula <= 0:
                row += red + text[idx % length] + reset
                idx += 1
            else:
                row += " "
        print(row)
        time.sleep(0.05)  # efecto suave de aparición

def main():
    os.system("cls" if os.name == "nt" else "clear")
    palabra = input("💬 Ingresa una palabra (por ejemplo 'skate'): ")
    print("\n💖 Generando tu corazón...\n")
    mensaje = "Te amodoro demasiado reina hermosa "
    print_heart(mensaje)
    print(f"\nTu palabra fue: {palabra}\n")

if __name__ == "__main__":
    main()
