def find_unique_element(arr):
    """
    Gibt das einzige Element in der Liste zurück, das genau einmal vorkommt.
    Alle anderen Elemente kommen exakt zweimal vor.

    Diese Lösung basiert auf XOR, das doppelte Zahlen aufhebt:
    a ^ a = 0,  a ^ 0 = a
    """

    if len(arr) % 2 == 0:
        raise Exception("Die Liste muss eine ungerade Anzahl an Elementen enthalten.")

    if not all(isinstance(x, int) for x in arr):
        raise TypeError("Alle Elemente müssen Ganzzahlen sein.")

    result = 0
    for num in arr:
        result ^= num  # hebt doppelte Zahlen auf

    return result