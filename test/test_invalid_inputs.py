import pytest
from src.find_unique import find_unique_element
# Ungültige oder problematische Eingaben – diese sollten Fehler auslösen, da sie gegen die Aufgabenbedingungen verstoßen.

def test_even_number_of_elements():
    with pytest.raises(Exception):
        find_unique_element([1, 2, 1, 2])  # Kein einzelnes Element → ungerade Anzahl fehlt

def test_non_integer_values():
    with pytest.raises(TypeError):
        find_unique_element([1, 2, 3, 2, "1"])  # String statt Integer

def test_multiple_unique_elements():
    # Annahme: Die Funktion prüft dies (optional absicherbar in deiner Implementierung)
    with pytest.raises(Exception):
        find_unique_element([1, 2, 3])  # drei eindeutige Elemente