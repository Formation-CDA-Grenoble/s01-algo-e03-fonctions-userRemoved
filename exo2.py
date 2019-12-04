def conditionalDouble(number):
    # Début de ton code
    
    # Fin de ton code
def test (fonction, pouet) :
     return fonction(fonction(pouet))

def multiplication(x):
     return x * 2

if x> 0 :  
    print(test(multiplication, 2))


# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -3),
)

for test in tests:
    print(f"L'appel  conditionalDouble({test[0]})  renvoie: {conditionalDouble(test[0])} (résultat attendu: {test[1]})")
