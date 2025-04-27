import random

# Problema del cumpleaños


def birthdayProblem(m: int) -> bool:
    birthdays = set()

    for i in range(m):
        day = random.randint(1, 365)
        if day in birthdays:
            # Hay por lo menos dos con el mismo día de cumpleaños, se ganó el juego.
            return True
        birthdays.add(day)

    return False  # Todos cumplen en días distintos.

# Calculo la probabiidad a partir de todos los casos ejecutados:


def empirical_probability(victories: int, total: int) -> float:
    return victories / total

# Calculo la probabilidad teórica a partir de lo aprendido en clase:


def probTheoricBirthdayProblem(m: int) -> float:
    prob_start = 1.0

    for i in range(m):
        prob_start *= (365 - i) / 365

    probability = 1 - prob_start
    return probability

# Simulaciones solicitadas:


def run_simulations(m: int, num_simulations: int):
    victories = 0
    defeats = 0

    for _ in range(num_simulations):
        if birthdayProblem(m):
            victories += 1
        else:
            defeats += 1

    return victories, defeats
