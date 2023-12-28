try:
    for i in range(88,189,79):
        print(i)
    n1 = int(input("Ingrese primer número:"))
except Exception as e:
    print("Error fatal")
    print(type(e))