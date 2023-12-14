class Perro:

    def habla(self):
        print("guau")

mi_perro = Perro()
print(type(mi_perro))
mi_perro.habla()
print(isinstance(mi_perro,Perro))