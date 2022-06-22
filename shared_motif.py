
from fasta_reader import *

path = "test_many.txt"
dna_list = (conv_list(path))
print(dna_list)

# == we will be comparing our shortest sequence to the rest of-
# the sequences in the list (this is why we will be sorting it).
sorted_list = sorted(dna_list)
shrt_dna = sorted_list[0] #shortest (iterable)
comp_dna = sorted_list[1:] #everything else

# == very brute force-way of finding the longest common string; 
# essentially, we check if each GROWING sequence of the smallest string of DNA-
# is found in the sequences we are comparing it to.
def sharedMotif(shrt_dna, comp_dna):
    motif = ""
    for i in range(len(shrt_dna)):
        for j in range(i, len(shrt_dna)):
            m = shrt_dna[i:j + 1] # to sort through the smallest seq one string at a time.
            found = False
            # we will compare the current sequence with each other sequence in the "compare" list.
            # if the current string is found in one of the sequences, we will check if the length-
            # of it is greater than our previous largest found motif. 
            for seq in comp_dna:
                if m in seq:
                    found = True
                else:
                    found = False
                    break
            if found and len(m) > len(motif): # if the new-found string is longer than our existing motif, we replace it with the new one.
                motif = m
                print(motif)
    print("shared motif:", motif)
    return (motif)


