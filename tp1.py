from pesado import cant_ceros, cant_unos, mas_unos_que_ceros, prefijo, es_pesado, densidad

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario según la siguiente codificación:
        A -> Cantidad de ceros;
        B -> Cantidad de unos;
        C -> Más unos que ceros;
        D -> Prefijo;
        E -> Es pesado;
        F -> Densidad;
        G -> Finalizar;
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás.
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Cantidad de ceros [s]')
    print('B. Cantidad de unos [s]')
    print('C. Más unos que ceros [s]')
    print('D. Prefijo [s,k]')
    print('E. Es pesado [n]')
    print('F. Densidad [n,m]')
    print('G. Finalizar')
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        s:str = input('Ingrese s: ')
        ceros:int = cant_ceros(s)
        print(f"En {s} hay {ceros} ceros.")

    elif opcion_seleccionada == 'B':
        s:str = input('Ingrese s: ')
        unos:int = cant_unos(s)
        print(f"En {s} hay {unos} unos.")
        
    elif opcion_seleccionada == 'C':
        s:str = input('Ingrese s: ')
        masUnos: bool = mas_unos_que_ceros(s)
        if(masUnos == True):
            print(f"El {s} tiene más unos que ceros.")
        else:
            print(f"El {s} no tiene más unos que ceros.")
         
    elif opcion_seleccionada == 'D':
        s:str = input('Ingrese s: ')
        k:int = int(input('Ingrese k: '))
        if(k>len(s)):
            print("Ingrese un numero menor o igual a la cantidad de caracteres en S")
        else:
            resultado: str = prefijo(s,k)
            print(f"El prefijo es {resultado}.")

    elif opcion_seleccionada == 'E':
        n:int = int(input('Ingrese n: '))
        if(n>=0):
            esPesado: bool = es_pesado(n)
            if(esPesado == True):
                print(f"El {n} es pesado.")
            else:
                print(f"El {n} no es pesado.")
        else:
            print("Ingrese un numero mayor o igual a 0")

    elif opcion_seleccionada == 'F':
        n:int = int(input('Ingrese n: '))
        m:int = int(input('Ingrese m: '))
        if(m<=n):
            print("n debe ser menor que m.")
        else:    
            resultado: float = densidad(n,m)
            print(f"La densidad de [{n},{m}) es {resultado}.")

    elif opcion_seleccionada == 'G':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'G':
        input('Presione ENTER para continuar.')
