from src.montyHall import monty_hall

#MontyHall
def execute_monty_hall(times : int):
    # Estrategia sin cambio de puerta
    not_change_door_win_counter = 0

    for i in range(times):
        game_result = monty_hall(False)
        if game_result:
            not_change_door_win_counter += 1

    # Estrategia con cambio de puerta
    change_door_win_counter = 0
    for i in range(times):
        game_result = monty_hall(True)
        if game_result:
            change_door_win_counter += 1

    return "El algoritmo se ejecutó" + " " + str(times) + " " + "veces" + "," + " " + "el participante ganó el auto sin cambio de puerta" + " " + str(not_change_door_win_counter) + " " + "veces" + " "  + "y" + " " + "el participante ganó el auto con cambio de puerta" + " " + str(change_door_win_counter) + " " + "veces"

#Menu interactivo para poder ejecutar el algoritmo.
print("Bienvenido a Monty Hall, a continuación elija la cantidad de veces que quiere ejecutar el algoritmo")
print("Escriba 1 si quiere ejecutar el algoritmo 1000 veces, 2 si quiere ejecutarlo 10000 veces o 3 si quiere ejecutarlo 100000 veces")

response = int(input())

posible_responses = [1, 2, 3]

while response not in posible_responses:
    print("Debe seleccionar una respuesta válida")
    response = int(input())

if response == 1:
    #1000 veces
    print(execute_monty_hall(1000))
elif response == 2:
    #10000 veces
    print(execute_monty_hall(10000))
elif response == 3:
    #100000 veces
    print(execute_monty_hall(100000))
