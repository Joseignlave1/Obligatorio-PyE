import secrets

def monty_hall(door_change : bool) -> bool:
    selected_doors = ["puerta1", "puerta2", "puerta3"]
    monty_posible_open_doors =["puerta1", "puerta2", "puerta3"]
    winner_door = secrets.choice(selected_doors)
    selected_door = secrets.choice(selected_doors)
    #El participante no cambia de puerta
    if not door_change:
        if selected_door == winner_door:
            print("El participante elige" + " " + selected_door)
            monty_posible_open_doors.remove(selected_door)
            print("Monty abre la puerta " " " + secrets.choice(monty_posible_open_doors))
            print("El auto esta en" + " " + selected_door)
            print("El participante gana el auto")
            win = True
        else:
            print("El participante elige" + " " + selected_door)
            monty_posible_open_doors.remove(selected_door)
            monty_posible_open_doors.remove(winner_door)
            print("Monty abre la puerta" + " " + secrets.choice(monty_posible_open_doors))
            print("El auto esta en" + " " + winner_door)
            print("El participante pierde el auto")
            win = False

    #Si el participante cambia de puerta
    else:
        if selected_door == winner_door:
            print("El auto esta en" + " " + winner_door)
            monty_posible_open_doors.remove(selected_door)
            monty_door_selected = secrets.choice(monty_posible_open_doors)
            print("Monty selecciona la puerta" + " " + monty_door_selected)
            monty_posible_open_doors.remove(monty_door_selected)
            selected_door = secrets.choice(monty_posible_open_doors)
            print("El participante elige" + " " + selected_door)
            print("El participante pierde el auto")
            win = False

        else:
            # El participante cambia de puerta.
            print("El participante elige" + " " + selected_door)
            monty_posible_open_doors.remove(selected_door)
            monty_posible_open_doors.remove(winner_door)
            monty_door_selected = secrets.choice(monty_posible_open_doors)
            print("Monty selecciona la puerta" + " " + monty_door_selected)
            selected_door = winner_door
            print("La nueva puerta elegida por el participante es la puerta" + " " + selected_door)
            print("El auto esta en" + " " + selected_door)
            print("El participante gana el auto")
            win = True

    return win
