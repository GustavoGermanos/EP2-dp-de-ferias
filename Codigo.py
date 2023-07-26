def transforma_base(lista):
    d = {}
    for dicio in lista:
        nivel = dicio['nivel']
        if nivel not in d:
            d[nivel] = []
        d[nivel].append(dicio)
    
        
    return d