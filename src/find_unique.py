def find_unique_element(arr):
    """
    Gibt das einzige Element in der Liste zurück, das genau einmal vorkommt.
    Alle anderen Elemente kommen exakt zweimal vor.

    Die Funktion zählt, wie oft jedes Element vorkommt,
    und gibt das zurück, das nur einmal enthalten ist.
    """

    # Eingabe prüfen: nur Ganzzahlen erlaubt
    for element in arr:
        if not isinstance(element, int):
            raise TypeError("Alle Elemente müssen Ganzzahlen sein.")

    # Eingabe prüfen: ungerade Anzahl erwartet (2n + 1)
    if len(arr) % 2 == 0:
        raise Exception("Die Liste muss eine ungerade Anzahl an Elementen enthalten.")

    # Für jedes Element zählen, wie oft es vorkommt
    for num in arr:
        if arr.count(num) == 1:
            return num
