from funciones import *

def ejecutar_menu():
    matriz = crear_array_bidimensional(5,5)
    while True:
        opcion = int(input("\nIngrese su opción:\n1-Cargar notas.\n2-Mostrar votos.\n3-Ordenar votos por nota promedio.\n4-Peores 3.\n5-Mayores promedio.\n6-Jurado malo.\n7-Sumatoria.\n8-Definir ganador.\nSu opción: "))

        match opcion:

            case 1:
                cargar_notas(matriz)

            case 2:
                mostrar_votos(matriz)

            case 3:
                ordenar_votos_promedio(matriz,input("Ingrese el orden (ascendente/descendente): "),"si")

            case 4:
                print(mostrar_peores_tres(matriz))

            case 5:
                mostrar_mayores_promedio(matriz)

            case 6:
                calcular_peores_promedios_jurados(matriz)

            case 7:
                mostrar_participante_sumatoria(matriz)

            case 8:
                calcular_ganador(matriz)
ejecutar_menu()