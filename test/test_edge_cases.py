from src.find_unique import find_unique_element

# Grenzfälle – sehr kleine Arrays oder ungewöhnliche, aber noch gültige Eingaben.
def test_only_one_element():
    assert find_unique_element([7]) == 7  # Nur ein einziges Element im Array

def test_element_in_middle():
    assert find_unique_element([2, 3, 4, 3, 2]) == 4  # Eindeutiges Element in der Mitte