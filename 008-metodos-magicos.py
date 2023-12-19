class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def habla(self):
        print(f"{self.nombre} dice: guau!")

    @classmethod
    def factory(cls):
        return cls("Perro feliz",5)
    

perro = Perro("chanchito",5)
perro.habla()
print(perro)  
