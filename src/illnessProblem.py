import random

def disease_test_simulation(n_simulations=1_000_000):
    true_positives = 0
    false_positives = 0
    total_positives = 0

    for _ in range(n_simulations):
        has_disease = random.random() < 0.0001   

        if has_disease:
            #Positivos reales
            test_positive = random.random() < 0.99  
        else:
            #Falsos positivos
            test_positive = random.random() < 0.02

        if test_positive:
            total_positives += 1
            if has_disease:
                true_positives += 1
            else:
                false_positives += 1

    if total_positives == 0:
        print("No hubo ningun test positivo")
        return 0

    print("Resumen de la simulación:")
    print(f"- Tests totales: {n_simulations}")
    print(f"- Positivos totales: {total_positives}")
    print(f"- Positivos reales: {true_positives}")
    print(f"- Falsos positivos: {false_positives}")
    print(f"- Probabilidad de estar realmente enfermo: {true_positives / total_positives:.5f}")

    return true_positives / total_positives