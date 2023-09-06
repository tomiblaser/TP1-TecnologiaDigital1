def cant_ceros(s:str) -> int:
    """
    Requiere: 
    Devuelve: La cantidad de ceros que se encuentran en el string
    """
    posicion : int = 0
    cantidadCeros: int = 0
    while posicion < len(s):
        if s[posicion] == "0":
            cantidadCeros = cantidadCeros + 1
        posicion = posicion + 1
    return cantidadCeros

def cant_unos(s:str) -> int:
    """
    Requiere: Nada
    Devuelve: La cantidad de unos que se encuentran en el string
    Modifica: Nada
    """
    posicion : int = 0
    cantidadUnos: int = 0
    while posicion < len(s):
        if s[posicion] == "1":
            cantidadUnos = cantidadUnos + 1
        posicion = posicion + 1
    return cantidadUnos

def mas_unos_que_ceros(s:str) -> bool:
    posicion : int = 0
    cantidadUnos: int = 0
    cantidadCeros: int = 0
    while posicion < len(s):
        if s[posicion] == "1":
            cantidadUnos = cantidadUnos + 1
        elif s[posicion] == "0":
            cantidadCeros = cantidadCeros + 1
        posicion = posicion + 1
    return cantidadUnos > cantidadCeros

def prefijo(s:str, k:int) -> str:
    posicion:int = 0
    prefijo:str = ""
    while posicion < k:
        prefijo += s[posicion]
        posicion += 1
    return prefijo


def entero_a_binario(numero:int)->str:
    resultado:str = ""
    while(numero > 0):
        resto = numero % 2
        numero = numero // 2
        resultado = str(resto) + resultado
    return resultado
   
def es_pesado(n: int) -> bool:
    binario = entero_a_binario(n)
    posicion: int = 0
    contadorUnos: int = 0
    contadorCeros: int = 0
    while(posicion < len(binario)):
        if(binario[posicion] == "0"):
            contadorCeros += 1
        elif(binario[posicion] == "1"):
            contadorUnos += 1
        posicion += 1
    return contadorUnos>contadorCeros

   
    
def densidad(n:int, m: int) -> float:   
    posicion: int = n
    cantidadDePesados : int = 0
    while (posicion < m):
        if(es_pesado(posicion)):
            cantidadDePesados += 1
        posicion += 1
    densidad:float = cantidadDePesados / (m-n)
    return densidad


   
"""    
print("")
print(cant_ceros("10010"))
print("")
print(cant_unos("10010"))
print("")
print(mas_unos_que_ceros("11001"))
print("")
print(mas_unos_que_ceros("10001"))
print("")
print(prefijo("DiTella",4))
print("")
print(es_pesado(57))
print("")
print(es_pesado(51))
print("")
print(densidad(29,33))

"""