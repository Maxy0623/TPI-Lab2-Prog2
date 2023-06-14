#Se importa el controlador
from controller.controller import Controller

#En esta funcion definimos el controller y invocamos unicamente a su función main(). Desde allí se maneja todo el sistema.
def main():
    controller = Controller()
    controller.menu()

if __name__ == "__main__":
    main()