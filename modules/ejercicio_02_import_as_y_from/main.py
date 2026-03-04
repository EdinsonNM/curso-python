# main.py

from operaciones import suma as add, resta as subtract

def main():
    num1 = 10
    num2 = 5
    
    resultado_suma = add(num1, num2)
    resultado_resta = subtract(num1, num2)
    
    print(f"La suma de {num1} y {num2} es: {resultado_suma}")
    print(f"La resta de {num1} y {num2} es: {resultado_resta}")

if __name__ == "__main__":
    main()