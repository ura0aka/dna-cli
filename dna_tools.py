from bio_structs import *
from collections import Counter
# =======================================================

# validate if data analysis in the given string contains in fact a DNA string
def validateSeq(seq):

    tmpSeq = seq.upper()
    for nuc in tmpSeq:
        if nuc not in Nucleotides:
            return False
        else:
            print(tmpSeq)
        return "DNA sequence: {DNA}".format(DNA = tmpSeq)


# count number of nucleotide types in sequence
def countNucFrequency(seq):

    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    print(tmpFreqDict)
    return "Number of nucleotides in sequence: {results} \n".format(results = tmpFreqDict)


# DNA to RNA transcription
def transcribeDNA(seq):

    rnaStr = (seq.replace("T", "U"))
    return "DNA/RNA transcription: {RNA} \n".format(RNA = rnaStr)


# Generates a reverse complement for original DNA string
def reverseComplement(seq):

    mapping = str.maketrans("ATCG", "TACG")
    return seq.translate(mapping)


# calculate the Guanine-Cytosine (nitrogenous-bases) percentage in our DNA sequence
def contentGC(seq):

    gc_content = int(((seq.count("C")) + (seq.count("G"))) / (len(seq)) * 100)
    return "The %G~C - Content of the DNA sequence is at: {gc}% \n".format(gc = gc_content)


# calculate GC-Content of specific sub-sections of the DNA sequence (K defines the length of the sub-sequence)
def contentGCSubseq(seq, k):

    for i in seq:
        sub_seq = [seq[i:i+k] for i in range(0, len(seq), k)]
    for j in sub_seq:
        gc_sub_content = int(((j.count("C")) + (j.count("G"))) / (len(j)) * 100)
        print("The %G~C - Content of the subsequence: ", j, "is : ", gc_sub_content,"%")
    return "\n"


# translate dna to amino-acids to form protein chain
def translateDNA(seq,  init_pos=0):

   return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq) -2, 3)]


# translate rna to amino-acids to form protein chain (same shit as the dna counterpart of this function)
def translateRNA(seq, init_pos=0):

    rnaStr = (seq.replace("T", "U"))
    return [RNA_Codons[rnaStr[pos:pos+3]] for pos in range(init_pos, len(rnaStr) -2, 3)]


# frequency of occurence of given amino acid in our DNA/RNA sequence
def aminoFreq(seq, amino_acid):

    temp_list = []
    for i in range(0, len(seq) -2, 3):
        if DNA_Codons[seq[i:i+3]] == amino_acid:
            temp_list.append(seq[i:i+3])
    freqDict = dict(Counter(temp_list))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return "Frequency of: [ {aa} ] in DNA/RNA sequence: {dict} ".format(aa = amino_acid, dict = freqDict)


# generate reading frames of our DNA sequence
def genReadingFrames(seq):

    frames = []
    frames.append(translateDNA(seq, 0))
    frames.append(translateDNA(seq, 1))
    frames.append(translateDNA(seq, 2))
    frames.append(translateDNA(reverseComplement(seq), 0))
    frames.append(translateDNA(reverseComplement(seq), 1))
    frames.append(translateDNA(reverseComplement(seq), 2))
    return frames


# find and return the promoter and it's type from DNA sequence
def findPromoter(seq):

    #list comprehension because I'm fucking lazy, I left a more comprehensible version of this function down below!
    promoters = [pro for pro in DNA_Promoters_BAC if pro in seq]
    #promoters = []
    #for pro in DNA_Promoters:
        #if pro in seq:
            #promoters.append(pro)
    return promoters


# iterate through frames, find the start codon (M) and start appending until stop codon (_)
def findStartCodon(seq):

    frames = genReadingFrames(seq)
    current_prot = []
    protein = []
    for frame in frames:
        for aa in frame:
            if aa == "_":

                if current_prot:
                    for p in current_prot:
                        protein.append(p)
                    current_prot = []
            else:

                if aa == "M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i] += aa
        return protein


        