try:
    n1 = int(input("Ingrese primer número:"))
except Exception as e:
    print("Error fatal")
    print(e.__getstate__)
else:
    print("No ocurrió ningún error")
finally:
    print("Imprimir siempre!")