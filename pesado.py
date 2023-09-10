def cant_ceros(s:str) -> int:
    """
    Requiere: Nada
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
    """
    posicion : int = 0
    cantidadUnos: int = 0
    while posicion < len(s):
        if s[posicion] == "1":
            cantidadUnos = cantidadUnos + 1
        posicion = posicion + 1
    return cantidadUnos

def mas_unos_que_ceros(s:str) -> bool:
    """
    Requiere: Nada
    Devuelve: True si hay mas unos que ceros. False si no hay mas unos que ceros
    """
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
    """
    Requiere: un string y luego un int que sea menor o igual a la longitud del string ingresado.
    Devuelve: Contando desde la izquierda, devolvera las primeras k (el int ingresado) caracteres del string ingresado
    """
    posicion:int = 0
    prefijo:str = ""
    while posicion < k:
        prefijo += s[posicion]
        posicion += 1
    return prefijo


def entero_a_binario(numero:int)->str:
    """
    Requiere: Un int mayor o igual a cero
    Devuelve: un string con el numero ingresado transformado a binario
    """
    resultado:str = ""
    if(numero==0):
        resultado="0"
    while(numero > 0):
        resto:int = numero % 2
        numero: int = numero // 2
        resultado = str(resto) + resultado
    return resultado
   
def es_pesado(n: int) -> bool:
    """
    Requiere: Un int mayor o igual a cero
    Devuelve: True si cada prefijo del numero int ingresado (expresado en binario) tiene mas unos que ceros. False en caso contrario.
    """
    binario: str = entero_a_binario(n)
    posicion: int = 0
    resultado: bool = True
    
    while(posicion < len(binario)):
        analizar: str = prefijo(binario, posicion+1)
        if(not mas_unos_que_ceros(analizar)):
            return False
        posicion += 1
    return resultado
        
   
    
def densidad(n:int, m: int) -> float:   
    """
    Requiere: 2 int donde el segundo debe ser mayor al primer numero ingresado.
    Devuelve: El resultado de la division entre la cantidad de numeros en el intervalo y la cantidad de numeros pesados en este
    """
    posicion: int = n
    cantidadDePesados : int = 0
    while (posicion < m):
        if(es_pesado(posicion)):
            cantidadDePesados += 1
        posicion += 1
    densidad:float = cantidadDePesados / (m-n)
    return densidad



print(densidad(2,3))