from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")

class Sesion(Model):
    def guardar(self):
        print("guardando archivo")

def guardar(entidad):
    entidad.guardar()

usuario = Usuario()
guardar(usuario)