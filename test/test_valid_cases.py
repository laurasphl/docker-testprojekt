from src.find_unique import find_unique_element

# Normale Eingaben mit erwartbarem Verhalten – also typische, korrekte Arrays mit genau einem eindeutigem Element.

def test_typical_case():
    assert find_unique_element([1, 2, 3, 2, 1]) == 3

def test_with_larger_numbers():
    assert find_unique_element([1001, 2002, 1001, 3003, 2002]) == 3003

def test_with_negative_numbers():
    assert find_unique_element([-1, -2, -1, -2, -3]) == -3