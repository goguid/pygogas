mascotas=["wolfgang","pelusa","pulga","copito","pelusa"]
print(mascotas.index("copito"))
print(mascotas.count("pelusa"))

for mascota in mascotas:
    print(mascota)

for mascota in enumerate(mascotas):
    print(mascota)


numeros = [2,76,33,4,1,6,8]
numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)


usuarios = [["juan",11],["esteban",41],["camilo",6]]


def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=True)
print(usuarios)


def ordena(elemento):
    return elemento[1]

usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)