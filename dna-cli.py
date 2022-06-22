import fasta_reader
from dna_tools import *
from Bio import SeqIO


path1 = "test_many.txt"
path2 = "test_one_dna.txt"
seqList = (fasta_reader.conv_list(path1))

seq_old = (fasta_reader.conv_list(path2))
seq = ""
for nuc in seq_old:
    seq += nuc



record_dict = SeqIO.to_dict(SeqIO.parse(path1, "fasta"))
# for k, v in record_dict.items():
#     print(k, v)



print(findStartCodon(seq))