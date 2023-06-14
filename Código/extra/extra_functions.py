#Se importa este módulo para verificar el SO del usuario
import os

#Dependiendo del SO, cls limpia la pantalla en windows y clear en linux
def clear_screen(): 
    os.system("cls" if os.name == "nt" else "clear")

#La funcion getch() del modulo msvcrt espera el ingreso de una tecla sin retornarla. En linux se configura la terminal en modo RAW y leer un caracter con la funcion sys.stdin.read(1)
def wait_key():
    if os.name == "nt": #Para Windows
        import msvcrt
        msvcrt.getch()
    else: #Para Linux
        import termios
        import tty
        import sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
