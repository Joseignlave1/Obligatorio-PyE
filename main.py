from src.illnessProblem import disease_test_simulation
from src.montyHall import monty_hall
from src.birthdayProblem import empirical_probability, probTheoricBirthdayProblem, run_simulations

def birthday_problem_menu():
    play = int(input("\n¿Quieres jugar al problema de cumpleaños?\n1. Sí\n0. No\n"))

    while play > 0:
        num_people = 0
        print("\nElige la cantidad de jugadores:")
        print("1. 10 jugadores")
        print("2. 20 jugadores")
        print("3. 30 jugadores")
        print("4. 40 jugadores")
        print("5. 50 jugadores")

        num_people_option = int(input("Opción: "))

        if num_people_option in [1, 2, 3, 4, 5]:
            num_people = num_people_option * 10
        else:
            print("Opción inválida. Por favor elige un número del 1 al 5.")
            continue

        print("\nElige la cantidad de repeticiones:")
        print("1. 1000 repeticiones")
        print("2. 10000 repeticiones")
        print("3. 100000 repeticiones")

        simulation_option = int(input("Opción: "))

        if simulation_option == 1:
            num_simulations = 1000
        elif simulation_option == 2:
            num_simulations = 10000
        elif simulation_option == 3:
            num_simulations = 100000
        else:
            print("Opción inválida. Por favor elige 1, 2 o 3.")
            continue

        victories, defeats = run_simulations(num_people, num_simulations)
        empirical_prob = empirical_probability(victories, num_simulations)
        theoretical_prob = probTheoricBirthdayProblem(num_people)

        print(f"\nResultados para {num_people} personas y {num_simulations} repeticiones:")
        print(f"Victorias: {victories}")
        print(f"Derrotas: {defeats}")
        print(f"Probabilidad empírica: {empirical_prob:.4f}")
        print(f"Probabilidad teórica: {theoretical_prob:.4f}")
        print(f"Diferencia (Empírica - Teórica): {abs(empirical_prob - theoretical_prob):.4f}")

        play = int(input("\n¿Quieres jugar otra vez?\n1. Sí\n0. No\n"))

    print("\n¡Gracias por jugar!")

def monty_hall_menu():
    print("\nBienvenido a Monty Hall, elige la cantidad de ejecuciones:")
    print("1. 1000 veces")
    print("2. 10000 veces")
    print("3. 100000 veces")

    response = int(input("Opción: "))

    while response not in [1, 2, 3]:
        print("Debe seleccionar una respuesta válida")
        response = int(input("Opción: "))

    if response == 1:
        times = 1000
    elif response == 2:
        times = 10000
    elif response == 3:
        times = 100000

    not_change_door_win_counter = 0
    for _ in range(times):
        if monty_hall(False):
            not_change_door_win_counter += 1

    change_door_win_counter = 0
    for _ in range(times):
        if monty_hall(True):
            change_door_win_counter += 1

    print(f"\nEl algoritmo se ejecutó {times} veces.")
    print(f"Ganó el auto SIN cambiar de puerta: {not_change_door_win_counter} veces.")
    print(f"Ganó el auto CAMBIANDO de puerta: {change_door_win_counter} veces.")

def illness_problem_menu():
    print("\nEjecutando simulación del problema de enfermedad...")
    disease_test_simulation()

def principal_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Problema de Cumpleaños")
        print("2. Juego Monty Hall")
        print("3. Problema de Enfermedad")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            birthday_problem_menu()
        elif opcion == '2':
            monty_hall_menu()
        elif opcion == '3':
            illness_problem_menu()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    principal_menu()
