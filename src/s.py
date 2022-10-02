from Bio import SeqUtils
from Bio.Seq import Seq


secuencia = Seq(
    "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

inicio = Seq("ATG")

pos = SeqUtils.nt_search(str(secuencia), inicio)
print(pos)

subsec = []
for i in range(1, len(pos) - 1):
    if i == len(pos):
        subsec.append(secuencia[pos[i]:])
    else:
        subsec.append(secuencia[pos[i]: pos[i + 1]])


print(subsec)
