import json
import random
import csv

with open("preguntas.json") as f:
    preguntas = json.load(f)

usuario = input("Ingresa el usuario: ")
nivel = 1
acumulado = 0

while nivel < 6:
    datos_nivel = [x for x in preguntas if x['nivel'] == nivel][0]
    preguntas_nivel = datos_nivel['preguntas']

    pregunta_aleatoria = random.choice(preguntas_nivel)

    # Mostrar pregunta
    print(f"\nNivel: {nivel}")
    print(f"Por {datos_nivel['premio']} puntos, de la categoría {pregunta_aleatoria['categoria']}, la pregunta es:")
    print(pregunta_aleatoria['pregunta'])

    # Ordenar aleatoriamente las respuestas
    lista_respuestas = [pregunta_aleatoria['respuesta'], pregunta_aleatoria['incorrecta1'], pregunta_aleatoria['incorrecta2'], pregunta_aleatoria['incorrecta3']]
    random.shuffle(lista_respuestas)

    # Mostrar opciones
    print(f"1. {lista_respuestas[0]}")
    print(f"2. {lista_respuestas[1]}")
    print(f"3. {lista_respuestas[2]}")
    print(f"4. {lista_respuestas[3]}")

    respuesta = int(input("Ingrese el número correspondiente a su respuesta: ").strip())

    # Respuesta correcta
    if lista_respuestas[respuesta-1] == pregunta_aleatoria['respuesta']:
        acumulado += datos_nivel['premio']
        print(f"¡Felicitaciones {usuario}, la respuesta fue correcta, tu premio es {datos_nivel['premio']}, y tu acumulado actual es {acumulado} puntos!\n")

    # Respuesta incorrecta
    else:
        print(f"Perdiste {usuario}, no te llevas nada esta vez :(")
        break

    # Desea continuar
    if nivel < 5:
        print("¿desea continuar? Y/n")
        respuesta = input().strip().upper()

        if respuesta == "N":
            print(f"¡Te llevaste {acumulado} puntos!")
            break

    nivel += 1

with open('registros.csv', 'a') as registros:
    writer = csv.writer(registros)
    writer.writerow([usuario, acumulado])