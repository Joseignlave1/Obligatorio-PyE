from src.illnessProblem import disease_test_simulation
from src.montyHall import monty_hall
from src.birthdayProblem import empirical_probability, probTheoricBirthdayProblem, run_simulations

# Tengo las opciones 10, 20, 30, 40, 50 personas.
# Cantidad de veces que simulo el problema: 1000, 10000, 100000

play = int(input("¿Quieres jugar?\n1. Sí\n0. No\n"))

while play > 0:

    num_people = 0

    print("\nElige la cantidad de jugadores:")
    print("1. 10 jugadores")
    print("2. 20 jugadores")
    print("3. 30 jugadores")
    print("4. 40 jugadores")
    print("5. 50 jugadores")

    num_people_option = int(input("Opción: "))
    match num_people_option:
        case 1:
            num_people = 10
        case 2:
            num_people = 20
        case 3:
            num_people = 30
        case 4:
            num_people = 40
        case 5:
            num_people = 50
        case _:
            print("Opción inválida. Por favor elige un número del 1 al 5.")
            continue  # Vuelve a preguntar sin salir del juego

    print("\nElige la cantidad de repeticiones:")
    print("1. 1000 repeticiones")
    print("2. 10000 repeticiones")
    print("3. 100000 repeticiones")

    simulation_option = int(
        input("¿Cuántas veces quieres simular? (elige 1 a 3): "))

    match simulation_option:
        case 1:
            num_simulations = 1000
        case 2:
            num_simulations = 10000
        case 3:
            num_simulations = 100000
        case _:
            print("Opción inválida. Por favor elige 1, 2 o 3.")
            continue

    # Ejecución de todo
    # Cantidad de victorias y derrtas en la simulación elegida.
    victories, defeats = run_simulations(num_people, num_simulations)
    # Probabilidad calculada a partir de la simulación.
    empirical_prob = empirical_probability(victories, num_simulations)
    # Probabilidad calculada a partir de la teoría.
    theoretical_prob = probTheoricBirthdayProblem(num_people)

    print(
        f"\nResultados para {num_people} personas y {num_simulations} repeticiones:")
    print(f"Victorias: {victories}")
    print(f"Derrotas: {defeats}")
    print(f"Probabilidad empírica: {empirical_prob:.4f}")
    print(f"Probabilidad teórica: {theoretical_prob:.4f}")
    print(
        f"Diferencia (Empírica - Teórica): {abs(empirical_prob - theoretical_prob):.4f}")

    # Preguntar si quiere volver a jugar
    play = int(input("\n¿Quieres jugar otra vez?\n1. Sí\n0. No\n"))

print("\n¡Gracias por jugar!")

# MontyHall


def execute_monty_hall(times: int):
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

    return "El algoritmo se ejecutó" + " " + str(times) + " " + "veces" + "," + " " + "el participante ganó el auto sin cambio de puerta" + " " + str(not_change_door_win_counter) + " " + "veces" + " " + "y" + " " + "el participante ganó el auto con cambio de puerta" + " " + str(change_door_win_counter) + " " + "veces"


# Menu interactivo para poder ejecutar el algoritmo.
print("Bienvenido a Monty Hall, a continuación elija la cantidad de veces que quiere ejecutar el algoritmo")
print("Escriba 1 si quiere ejecutar el algoritmo 1000 veces, 2 si quiere ejecutarlo 10000 veces o 3 si quiere ejecutarlo 100000 veces")

response = int(input())

posible_responses = [1, 2, 3]

while response not in posible_responses:
    print("Debe seleccionar una respuesta válida")
    response = int(input())

if response == 1:
    # 1000 veces
    print(execute_monty_hall(1000))
elif response == 2:
    # 10000 veces
    print(execute_monty_hall(10000))
elif response == 3:
    # 100000 veces
    print(execute_monty_hall(100000))

# illness problem

disease_test_simulation()
