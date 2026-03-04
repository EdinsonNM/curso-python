# main.py

from paquete_utilidades.calculos import suma, resta

def main():
    a = 10
    b = 5
    resultado_suma = suma(a, b)
    resultado_resta = resta(a, b)
    
    print(f"La suma de {a} y {b} es: {resultado_suma}")
    print(f"La resta de {a} y {b} es: {resultado_resta}")

if __name__ == "__main__":
    main()