def cascadeIsPositive(list):
    # Début de ton code
    pass
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [True, True, True]),
    ([10], [True]),
    ([1, -1, 1, -1, 1], [True, False, True, False, True]),
    ([-12, 0, 50], [False, None, True]),
)

for test in tests:
    print(f"L'appel  cascadeIsPositive({test[0]})  renvoie: {cascadeIsPositive(test[0])} (résultat attendu: {test[1]})")
