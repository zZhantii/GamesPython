import random

# Juego 1: Adivina el número
def option_1 ():
    print("Adivina el número seleccionado...\n \n\t¡Bienvenido a Adivina un número!")
    print("\tTendrás tres intentos para lograr adivinar el número, ¡mucha suerte!\n")

    numberRandom = random.randint(1, 10)
    attempts = 0
    attemptsFailed = 2

    while attempts < 3:

        try:
            numberUser = int(input("Introduce un número entre 1 y 10: "))

            if numberUser is None:
                print("\tError: Debes de introducir un numero")
            elif numberUser < 1 or numberUser > 10:
                print("\tError: Debes de introducir un número entre 1 y 10")
            else:
                if numberRandom == numberUser:
                    print(f'\nFelicidades, has acertado el número aleatorio, el número aleatorio era {numberRandom}\n')
                    break
                elif numberUser < numberRandom:
                    print(f'\n\tEl número que has introducido es menor que el número aleatorio \n\tEl número que has dicho es el {numberUser} \n\tTe quedan {attemptsFailed} intento(s).\n')
                    attempts += 1
                    attemptsFailed -= 1
                else:
                    print(f'\n\tEl número que has introducido es mayor que el número aleatorio \n\tEl número que has dicho es el {numberUser} \n\tTe quedan {attemptsFailed} intento(s).\n')
                    attempts += 1
                    attemptsFailed -= 1
        except ValueError: 
            print("\tError: Solo puedes introducir un numero, no se puede letras ni numeros con decimales")

        if attempts == 3:
            print(f'Lo siento, has agotado los intentos, el número aleatorio era {numberRandom}\n')

# Juego 2:  Piedra, papel o tijera
def option_2():
    print("Piedra, Papel o Tijeras seleccionado...\n \n\t¡Estas jugando a Piedra, Papel y tijeras!")
    print("\tEl primero que llegue a 3 puntos gana\n")

    pointsUser = 0
    pointsNPC = 0

    print("\tComienza la partida\n")
    
    while  pointsUser < 3 and pointsNPC < 3:
        try:
            optionUser = int(input("Introduce un numero del 1 al 3: "))
            optionValueUser = ""

            if optionUser < 1 or optionUser > 3:
                print("\tError: Debes de introducir un número entre 1 y 3")
            else:
                print("\t1. Piedra \n\t2. Papel \n\t3. Tijeras\n")

                if optionUser == 1:
                    optionValueUser = "Piedra"
                elif  optionUser == 2:
                    optionValueUser = "Papel"
                elif optionUser == 3:
                    optionValueUser = "Tijeras"

                optionNPC = random.randint(1, 3)
                optionValueNPC = ""

                if optionNPC == 1:
                        optionValueNPC = "Piedra"
                elif  optionNPC == 2:
                        optionValueNPC = "Papel"
                elif optionNPC == 3:
                    optionValueNPC = "Tijeras"

                if optionValueNPC == optionValueUser:
                    print(f'\t¡Empate! Ambos elegiste {optionValueUser}')
                    print(f'\tPuntos de usuario: {pointsUser}, Puntos del NPC: {pointsNPC}\n')
                elif optionValueUser == "Papel" and  optionValueNPC == "Tijeras" or optionValueUser == "Tijeras" and optionValueNPC == "Piedra" or optionValueUser == "Piedra" and optionValueNPC == "Papel":
                    print(f'\t¡Gana el NPC! El NPC ha elegido {optionValueNPC} y el usuario ha elegido {optionValueUser}')
                    pointsNPC += 1
                    print(f'\tPuntos de usuario: {pointsUser}, Puntos del NPC: {pointsNPC}\n')
                elif optionValueUser == "Papel" and  optionValueNPC == "Piedra" or optionValueUser == "Piedra" and optionValueNPC == "Tijeras" or optionValueUser == "Tijeras" and optionValueNPC == "Papel":
                    print(f'\t¡Gana el usuario! El usuario ha elegido {optionValueUser} y el NPC ha elegido {optionValueNPC}')
                    pointsUser += 1
                    print(f'\tPuntos de usuario: {pointsUser}, Puntos del NPC: {pointsNPC}\n')

                if pointsUser == 3:
                    print(f'\n\t¡Felicidades! Has ganado la partida con un marcador de { pointsUser} - {pointsNPC}\n')
                elif pointsNPC == 3:
                    print(f'\n\t¡Lo siento! Has perdido la partida con un marcador de { pointsUser} - {pointsNPC}\n')
        except ValueError: 
                print("\tError: Solo puedes introducir un numero, no se puede letras ni numeros con decimales")

# Juego 3:  El ahorcado
def option_3():
    print("El ahorcado seleccionado...\n \n\t¡Estas jugando al ahorcado!")
    print("\tTienes dos intentos para adivinar la palabra\n")

    with open("palabras.txt", "r") as palabra:
        palabras = palabra.readline().split(";")
        num_palabras = len(palabras)
        indice_aleatorio = random.randint(0, num_palabras - 1)
        palabra_secreta = palabras[indice_aleatorio].strip().upper()

    palabra_oculta = ["_"] * len(palabra_secreta)

    attempts = len(palabra_secreta) * 2

    print(" ".join(palabra_oculta))

    while attempts > 0:

        letra = input("Introduce una letra: ").upper()

        if letra is None:
            print("Error: Debes de escribir una letra")
        elif len(letra) > 1:
            print("Error: Solamente puedes escribir una letra")
            # Comprueba si es una letra
        elif letra.isalpha() == False:
            print("\tError: Solo puedes introducir un letra, no se puede numeros")
        else:
            if letra in palabra_secreta:
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        palabra_oculta[i] = letra
                print(" ".join(palabra_oculta))
            else:
                attempts -= 1
                print(f"\t\nIncorrecto, te quedan {attempts} intentos\n")
                print(" ".join(palabra_oculta))

            if "_" not in palabra_oculta:
                print("\nFelicidades, has ganado\n")
                break

            if attempts == 0:
                print(f"\nLo siento, has perdido. La palabra era {palabra_secreta}\n")
                break

# Menu para eleccion del juego
GameMenu = {
    "1": option_1,
    "2": option_2,
    "3": option_3
}

while True:
    print("Bienvenido al menu de opciones, escoge cualquier de las tres opciones para jugar\n") 
    print("\tJuegos:")
    print("\t1. Adivina el número \n\t2. Piedra, Papel o Tijeras \n\t3. Ahorcado \n\t4. Salir\n")

    option = input("Seleciona una juego: ")
    
    if option in GameMenu:
        # Selecion del menu para derivar a las funciones
        GameMenu[option]()
    elif option ==  "4":
        print("¡Hasta Luego!")
        break
    else:
        print("\nError: Debes de selecionar un número valido")