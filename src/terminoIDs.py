
'''
NAME
    buscador de IDs de cada DB

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que genera un archivo con los IDs de cada DB que coincida con un termino generado
    * Si no se encontraron bases de datos para su termino entonces el archivo final no lo incluira

USAGE
    py src/terminoIDs.py 

ARGUMENTS
'''
# importar librerias
from Bio import Entrez
import re

# ingresar el email
Entrez.email = 'aldogp@lcg.unam.mx'

# crear el diccionario inicial
dicOrganismos = {'Mus Musculus': [
    'TrnM', 'ND4L', 'ND3'], 'Drosophilla Melanogaster': ['Prim1', 'PolG1', 'Atg6']}


def getTermino():  # funcion para obtener el termino
    def getGenes(x):  # funcion para obtener la lista de genes de cada organismo en formato
        genes = ''
        for i in range(0, len(dicOrganismos[x])):
            genes += F'{dicOrganismos[x][i]}[Gene] OR '
        # al final al que quitar el OR sobrante
        genes = re.sub(' OR $', '', genes)
        return(genes)

    # crear el vector de los terminos
    terminos = []
    # recorrer el diccionario por medio de sus keys
    for x in dicOrganismos.keys():
        terminos.append(F'{x}[Orgn] AND ({getGenes(x)})')

    # regresar el/los termino/s
    return(terminos)


terminos = getTermino()


def getIds():
    def getDatabases():  # funcion para obtener las bases de dato de cada organismo
        # vector que guardara los vectores con las DBs
        dB_Organismos = []

        # recorrer los terminos para buscarlos
        for t in terminos:
            handle = Entrez.egquery(term=t)
            result = Entrez.read(handle)
            # vector que guarda las DBs
            databases = []
            # recorrer cada item del vector con los resultados
            for x in result['eGQueryResult']:
                # ver si la base de datos en cuestion si tuvo resultados
                if x['Count'] != '0' and x['Count'] != 'Error' and x['Status'] == 'Ok':
                    # agregarla de ser cierto
                    databases.append(x['DbName'])
            # meter el vector con las BDs al vector de los organimos
            dB_Organismos.append(databases)
        return(dB_Organismos)

    # llamar a funcion para obtener las DBs
    db_Organismos = getDatabases()
    n = 0
    # obtener las keys de los organismos en lista
    keys = list(dicOrganismos.keys())
    # abrir el archivo de output
    out = open('results/IdDatabases.txt', 'w')
    # recorrer los vectores en db_Organismos
    for databases in db_Organismos:
        if databases != []:
            out.write(F'{keys[n]}\n')
            output = {F'Organismo': F'{keys[n]}'}
            # recorrer las databases
            for x in databases:
                handle = Entrez.esearch(db=x, term=terminos[n])
                result = Entrez.read(handle)
                ids = result['IdList']
                out.write(F'{x}: {ids}\n')
                temp = {F'{x}': ids}
                output.update(temp)
            n += 1
    # cerrar el archivo
    out.close()
    # indicar al usuario del output
    print('se creo un archivo de salida: results/IdDatabases.txt\n')
    return(output)


dic = getIds()


def filtrado():  # funcion que hace el filtrado de las bases de datos que nos interesan
    for x in list(dic.keys()):
        if x == 'pubmed' or x == 'pmc' or x == 'mesh' or x == 'books' or x == 'ncbisearch' or x == 'Organismo':
            continue
        else:  # eliminar si no coincide con las bases de interes
            del dic[x]
    return(dic)


# llamar a la funcion
dicFiltrado = filtrado()
