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

    return "El participante ganó el auto sin cambio de puerta" + " " + str(not_change_door_win_counter) + " " + "veces" + " "  + "y" + " " + "el participante ganó el auto con cambio de puerta" + " " + str(change_door_win_counter) + " " + "veces"

#1000 veces
#print(execute_monty_hall(1000))

#10000 veces
#print(execute_monty_hall(10000))

#100000 veces
#print(execute_monty_hall(100000))


