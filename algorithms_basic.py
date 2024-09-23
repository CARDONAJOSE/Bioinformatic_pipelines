#lecture archives fasta
from Bio import SeqIO

for record in SeqIO.parse("example.fasta", "fasta"):
    print(record.id)
    print(record.seq)



#lecture archives Genbank
from Bio import SeqIO

for record in SeqIO.parse("example.gb", "genbank"):
    print(record.id)
    print(record.description)
    print(record.seq)

# calcule de % GC contenu dans une secuence

from Bio.SeqUtils import GC

gc_content = GC(dna_seq)

print("GC Content:", gc_content, "%")

