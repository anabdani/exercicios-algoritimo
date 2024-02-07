def verificar_triangulo(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        return True
    else:
        return False

def main():
    print("Digite o comprimento dos três segmentos de reta:")
    a = float(input("Comprimento da primeira reta: "))
    b = float(input("Comprimento da segunda reta: "))
    c = float(input("Comprimento da terceira reta: "))

    if verificar_triangulo(a, b, c):
        print("É possível formar um triângulo com essas retas.")
    else:
        print("Não é possível formar um triângulo com essas retas.")

if __name__ == "__main__":
    main()
    