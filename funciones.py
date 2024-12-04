import random

def crear_array_bidimensional (columnas:int,filas:int)-> list:
    '''
    Crea un array bidimensional de unas dimensiones deseadas.\n
    Se toma como primer parámetro la cantidad de columnas y como segundo la cantidad de filas.\n
    Retorna la matriz deseada.
    '''
    array = [[0]* columnas for _ in range (filas)]

    return array

def cargar_notas(matriz:list)->None:
    '''
    Permite agregar manualmente las notas de los participantes.\n
    Ingresamos como parámetro la matriz.\n
    No retorna ninún valor en específico.
    '''
    reiniciar_valores(matriz) #No se me pisa el acumulador de votos, me lo suma con la anterior carga de notas.
    participante = 1
    for i in range (len(matriz)):
        for j in range (len(matriz[i])-1): #La ultima columna no la recorro.
            if j == 0:
                matriz[i][j] = participante #Este será el número de participante.
                participante += 1 #Inicia en 1 y se va sumando automáticamente.
            else:
                matriz[i][j] = validar_rango(int(input(f"Ingrese el voto del jurado {j} para el participante N°{matriz[i][0]}: ")),1,100) #Validación del rango.
                matriz[i][4] += matriz[i][j] #Se van acumulando los votos en la fila de cada participante.

def mostrar_votos(matriz:list)->None:
    '''
    Presenta la matriz en un formato lindo y legible.\n
    Se ingresa como parámetro la matriz.\n
    No retorna un valor en específico.
    '''
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):

            match j:
                case 0: #Número de participante.
                    print(f"Participante Nro {matriz[i][j]}:")
                case 1|2|3: #Votos de los jurados.
                    print(f"Nota Jurado {j}: {matriz[i][j]}")
                case 4: #Nota promedio.
                    print(f"Nota promedio: {matriz[i][j]/3:.2f}")
        print("-"*55)

def ordenar_votos_promedio(matriz:list,orden:str,mensaje:str)->list:
    '''
    Ordena un array bidimensional de enteros según el orden especificado.\n
    Ingresa como parámetro un array bidimensional, el orden (ascendente o descendente) y si se quiere imprimir el mensaje.\n
    Retorna ese mismo array ordenado.
    '''
    #Usamos método burbuja.
    if orden == "ascendente":
        for i in range (len(matriz)-1):
            for j in range (i+1,len(matriz)):
                if matriz[i][4] < matriz[j][4]: #Se comparan los promedios, por eso índice 4.
                    temp = matriz[i] #Se guarda temporalmente el número para pisarlo.
                    matriz[i] = matriz[j] #Intercambio de "posiciones".
                    matriz[j] = temp #Asignamos el valor temporal que guardamos antes.

    elif orden == "descendente":
        for i in range (len(matriz)-1):
            for j in range (i+1,len(matriz)):
                if matriz[i][4] > matriz[j][4]:
                    temp = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = temp

    if mensaje == "si":
        print("Se ha ordenado adecuadamente.")
    return matriz

def mostrar_peores_tres(matriz:list)->str:
    '''
    Obtenemos los peores tres promedios.\n
    Ingresamos como parámetro la matriz.\n
    Retorna un mensaje con los participantes de peores promedio.\n
    '''
    ordenar_votos_promedio(matriz,"ascendente","no") #Reutilizamos la función, pero sin que se imprima el mensaje de que se ha ordenado.

    mensaje = f'''Los peores 3 participantes fueron:\nParticipante N°{matriz[2][0]}\nParticipante N°{matriz[3][0]}\nParticipante N°{matriz[4][0]}''' #Seleccionamos a los últimos participantes luego del ordenamiento.

    return mensaje

def calcular_promedio_general(matriz:list)->int:
    '''
    Calculamos cuál fue el promedio entre todos los participantes.\n
    Ingresamos como parámetro la matriz.\n
    Retorna el promedio final.
    '''
    suma = 0
    for i in range (len(matriz)):
        suma += matriz[i][4]
    resultado = suma / 5 / 3
    resultado = resultado
    return resultado

def mostrar_mayores_promedio(matriz:list)->None:
    '''
    Obtenemos cuáles fueron los mejores promedios.\n
    Ingresamos como parámetro la matriz.\n
    No retorna un valor en específico, imprime un mensaje por consola.
    '''
    promedio = calcular_promedio_general(matriz) #Almacenamos el promedio general de todos los participantes para compararlo.
    flag = 0
    mensaje = f"Los mejores promedios fueron:\n"

    for i in range (len(matriz)):
        if matriz[i][4] / 3 >  promedio: #Comparamos el promedio de cada participante con el promedio general.
            mensaje += f"- Participante N°{matriz[i][0]}\n" #En caso de ser mayor, lo agregamos.
            flag = 1

    if flag == 0: #En caso de que ninguno supere el promedio general.
        mensaje = f"Ningún participante supera el promedio general."

    print(mensaje)

def mostrar_participante_sumatoria(matriz:list)->None:
    '''
    Obtenemos los participantes que superen la nota ingresada.\n
    Ingresamos como parámetro la matriz.\n
    No retorna un valor en específico.
    '''
    flag = 0 #Bandera para el mensaje en caso de que no se haya encontrado ninguno
    numero_ingresado = validar_rango(int(input("Ingrese un número del 3 al 300: ")),3,300)

    for i in range (len(matriz)):
        if matriz[i][4] == numero_ingresado: #Comparamos la sumatoria de los votos con el 
            print(f"El participante {matriz[i][0]} ha recibido esa cantidad de votos.")
            flag = 1

    if flag == 0:
        print("Ningún participante tuvo esa cantidad de votos.")

def validar_rango(numero_ingresado:int,numero_minimo:int,numero_maximo:int)->int:
    '''
    Validamos que un número esté dentro del rango que deseamos. Lo vuelve a pedir si no está dentro del rango.\n
    Ingresamos como parámetro el número ingresado, el valor mínimo y máximo en donde puede estar.\n
    Retorna el número ingresado.
    '''
    while numero_ingresado < numero_minimo or numero_ingresado > numero_maximo:
        numero_ingresado = int(input("[FUERA DE RANGO] Ingrese el número nuevamente: "))
    return numero_ingresado

def reiniciar_valores(matriz:list)->None:
    '''
    Me vuelve a 0 todos los valores de la matriz.\n
    Ingresamos como parámetro la matriz.\n
    No retorna un valor en específico.
    '''
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz[i][j] = 0

def sumar_numeros(numero_uno:int,numero_dos:int,numero_tres:int)->int:
    '''
    Realiza la suma de tres números.\n
    Se ingresa por parámetro los mismos.\n
    Retorna el resultado de la operación.
    '''
    suma = numero_uno + numero_dos + numero_tres
    return suma

def sumar_notas_jurados(matriz:list)->tuple:
    '''
    Obtenemos cuál fue la cantidad de votos de cada jurado.\n
    Se ingresa como parámetro la matriz.\n
    Retorna el acumulador de votos de cada jurado.
    '''
    acumulador_jurado_uno = 0
    acumulador_jurado_dos = 0
    acumulador_jurado_tres = 0
    for i in range (len(matriz)):
        acumulador_jurado_uno += matriz[i][1]
        acumulador_jurado_dos += matriz[i][2]
        acumulador_jurado_tres += matriz[i][3]
    
    return(acumulador_jurado_uno,acumulador_jurado_dos,acumulador_jurado_tres)

def promediar_notas_jurados(matriz:list)->list:
    '''
    Promediamos la nota de cada jurado.\n
    Ingresamos como parámetro la matriz.\n
    Retorna un array con el promedio de cada jurado.
    '''
    notas = sumar_notas_jurados(matriz)
    notas_promedio = []
    for i in range (len(notas)):
        notas_promedio.append(notas[i]/5)
    return notas_promedio

def calcular_peores_promedios_jurados(matriz:list)->None:
    '''
    Obtenemos cuál o cuáles fueron los jurados con peores notas promedio.\n
    Ingresamos como parámetro la matriz.\n
    No retorna un valor en específico.
    '''
    promedio = promediar_notas_jurados(matriz) #Almacenamos los promedios en una variable.
    menor_nota = promedio[0]  # Inicializamos con el primer valor
    menor_promedio = "Jurado 1" #Por el momento es el menor jurado.

    for i in range(1, len(promedio)):
        if promedio[i] < menor_nota: #Comparamos la nota promedio con la menor nota hasta el momento.
            menor_nota = promedio[i] #Ahora pasa a ser esa la menor nota.
            menor_promedio = f"Jurado {i+1}"  #En caso de haber uno con menor nota promedio, pisa a los anteriores.
        elif promedio[i] == menor_nota:
            menor_promedio += f", Jurado {i+1}"  #En caso de empate, se agrega ese jurado.

    print(f"El jurado o jurados con la menor nota promedio fueron:\n{menor_promedio}\n")

def obtener_promedio_jugadores(matriz:list)->list:
    '''
    Recorremos la matriz y guardamos la información de la nota promedio.\n
    Ingresamos como parámetro la matriz.\n
    Retorna un array con el promedio de cada participante por separado.
    '''
    promedio = []
    for i in range (len(matriz)):
        promedio.append(matriz[i][4]/3)
    return promedio

def calcular_ganador(matriz:list)->None:
    '''
    Obtenemos el ganador de la competencia.\n
    Ingresamos como parámetro la matriz.\n
    No retorna un valor en específico, se imprime el ganador por consola.
    '''
    promedio = obtener_promedio_jugadores(matriz)  #Almacenamos los promedios de todos los jugadores.
    mayor_nota = promedio[0]  #Inicializamos con el primer valor.
    acumulador_ganadores = [1]  #Por el momento el participante 1 es el ganador.
    votos_jurado = []
    ganador = None

    #Comparamos al primer participante con los demás.
    for i in range(1, len(promedio)):
        if promedio[i] > mayor_nota:  # Si encontramos un promedio mayor.
            mayor_nota = promedio[i]  # Actualizamos el mayor promedio.
            acumulador_ganadores = [i+1]  # Reiniciamos la lista de ganadores con el actual.
        elif promedio[i] == mayor_nota:  #En caso de empate.
            acumulador_ganadores.append(i+1)  #Añadimos al participante empatado.

    if len(acumulador_ganadores) > 1: #En caso de haber más de un ganador.
        for i in range (1,4): #Pedimos el voto a los 3 jurados.
            flag = 0 #Bandera para si el voto es válido.
            voto = int(input(f"Ingrese el voto del jurado {i} {acumulador_ganadores}: "))
            while flag == 0:
                for j in range (len(acumulador_ganadores)):
                    if voto == acumulador_ganadores[j]:
                        votos_jurado.append(voto)
                        flag = 1

                if flag == 0: #Si el voto no está dentro de las posibles opciones.
                    voto = int(input(f"[ERROR] Ingrese el voto del jurado {i} nuevamente: ")) 

        if len(votos_jurado) > 1:
            bandera = 0
            for i in range (len(votos_jurado)):
                for j in range (len(votos_jurado)):
                    if i != j: #Se comparan los diferentes índices.
                        if votos_jurado[i] == votos_jurado[j]: #Si los participantes son iguales.
                            ganador = votos_jurado[i] #Se determina al ganador.
                            bandera = 1 #Cambia la bandera.

            if bandera == 0: #En caso de no encontrar votos iguales.
                ganador = random.choice(votos_jurado) #Selecciona random dentro de los votos de los jurados.

    else:
        ganador = acumulador_ganadores[0]

    print(f"El ganador es el participante N°{ganador}\n")
