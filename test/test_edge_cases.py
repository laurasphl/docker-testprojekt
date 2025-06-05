from src.find_unique import find_unique_element

# Grenzfälle – sehr kleine Arrays oder ungewöhnliche, aber noch gültige Eingaben.
def test_only_one_element():
    assert find_unique_element([7]) == 7  # rufe die Funktion find_unique_element([7]) auf und prüfe, ob das Ergebnis gleich 7 ist.

def test_element_in_middle():
    assert find_unique_element([2, 3, 4, 3, 2]) == 4  