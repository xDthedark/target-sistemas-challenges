# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    import sys
    numero = int(sys.argv[1])
    fibonacci(numero)
