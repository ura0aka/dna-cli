# == COLORS ==
A = "\033[1;32m"
C = "\033[1;31m"
G = "\033[1;35m"
T = "\033[1;36m"
U = "\033[1;36m"
colorless = "\033[0;0m"
# change colors for each nucleotide
def nucleotideColors(seq):
    nucColors = {"A": A ,
                 "C": C ,
                 "G": G ,
                 "T": T ,
                 "U": U,
                 "nothing": colorless}
    tmpStr = ""
    for nuc in seq:
        if nuc in nucColors:
            tmpStr += nucColors[nuc] + nuc
        else:
            tmpStr += nucColors["nothing"] + nuc
    return tmpStr + colorless