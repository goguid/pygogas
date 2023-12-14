from pprint import pprint 

string = "Hola mundo este es mi string"
print(string)

def quitar_espacios(texto):
    return [char for char in texto if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char]+=1
        else:
            chars_dict[char]=1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],reverse=True
    )

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]]=orden[1]
    return respuesta

def crea_mensaje(diccionario):
    mensaje = "Los valores que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje

string_sin_espacios = quitar_espacios(string)
contados = cuenta_caracteres(string_sin_espacios)
contados_ordenados = ordena(contados)
mayores = mayores_tuplas(contados_ordenados)
mensaje = crea_mensaje(mayores)

print(string_sin_espacios)
pprint(contados,width=1)
print(contados_ordenados)
print(mayores)
print(mensaje)