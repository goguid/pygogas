class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau")

    @classmethod
    def factory(cls):
        return cls("Perro feliz",5)



mi_perro = Perro("chanchito",3)
print(mi_perro.patas)
print(mi_perro.nombre)
print(mi_perro.habla())
print(Perro.habla())
print(Perro.factory().nombre)