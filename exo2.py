def conditionalDouble(number):
    # Début de ton code
    for test in tests : 
        if test [1] >= 0 :  
            print (test[1::2]) 
    # Fin de ton code



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -3),
)

for test in tests:
    print(f"L'appel  conditionalDouble({test[0]})  renvoie: {conditionalDouble(test[0])} (résultat attendu: {test[1]})")
