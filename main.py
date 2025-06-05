def find_unique_element(arr):
    """Findet das Element, das nur einmal vorkommt, während alle anderen zweimal erscheinen."""
    unique = 0
    for num in arr:
        unique ^= num  # XOR hebt doppelte Zahlen auf
    return unique
