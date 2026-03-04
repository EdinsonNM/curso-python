# main.py

from modulo import saludar, despedir


def main():
    nombre = input("Ingrese su nombre: ")
    saludar(nombre)
    despedir(nombre)


if __name__ == "__main__":
    main()
