from Bio import SeqIO

# == read FASTA file and convert it into a list ==
def conv_list(path):
    reads_list = []
    handle = open(path, "r")

    for record in SeqIO.parse(handle, "fasta"):
        sequence = []                          
        seq = ""                               
        for nt in record.seq:                  
            seq += nt                          
        reads_list.append(seq)                  
    handle.close()
    return reads_list

    
#print(conv_list(path))

# record_dict = SeqIO.to_dict(SeqIO.parse(path, "fasta"))
# for k, v in record_dict.items():
#     print(k, v)