def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    diccionario = {}
    longitud = len(samples)
    for number in samples:
        if number in diccionario:
            diccionario[number] += 1
        else:
            diccionario[number] = 1

    lista_final = []
    for num,frec in diccionario.items():
        lista_final.append((num,frec/longitud))
    
    return lista_final


    pass