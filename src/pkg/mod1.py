# funcion para sacar porcentaje de AT y GC
def porcentaje_ATGC(seq):
    # contar longitud de la secuencia
    long = len(seq)
    # hacer calculos
    porcentaje_AT = ((seq.count('A') + seq.count('T')) / long * 100)
    porcentaje_GC = ((seq.count('G') + seq.count('C')) / long * 100)
    print(F"AT = {porcentaje_AT} %\nGC = {porcentaje_GC} %")
    return 0
