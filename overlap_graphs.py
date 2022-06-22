import itertools
from custom_fasta_reader import *

# check if reads overlap depending on the length of the shared gene
def isOverlap(r1, r2, k):
    return r1[-k:] == r2[:k]

# # == test cases ==
# print(overlap('AAATTTT', 'TTTTCCC', 3))
# # Output: True
# print(overlap('AAATTTT', 'TTTTCCC', 5))
# # Output: False
# print(overlap('ATATATATAT', 'TATATATATA', 4))
# # Output: False
# print(overlap('ATATATATAT', 'TATATATATA', 5))
# # Output: True


# return longest overlap sequence possible 
def maxOverlap(r1, r2):
    long_overlap = ""

    for i in range(len(r1)):
        for j in range(len(r2)):
            temp = 0
            match = ""
            while (i + temp < len(r1)) and (j + temp < len(r2)) and (r1[i+temp] == r2[j+temp]):
                match += r2[j+temp]
                #this switches rows and column by 1 position, basically checking if the next char
                #in r1 matches r2
                temp += 1
            if len(match) > len(long_overlap):
                long_overlap = match

    #choose to return matching overlap in str form or its length
    return len(long_overlap), long_overlap

# # == test cases ==
# print(max_overlap('AAATTTT', 'TTTTCCC'))
# # Expected output: 4
# print(max_overlap('ATATATATAT', 'TATATATATA'))
# # Expected output: 9


reads_dict = readFile ("test_many.txt")
reads_dict = FASTA_dict
#print(reads_dict)

# return an adjacency list of all reads that overlap at a specified length
def overlap_graph(reads_dict, k):
    adjacency_list = []
    
    for v1_labl, v2_labl in itertools.combinations(reads_dict, 2):
        v1_read, v2_read = reads_dict[v1_labl], reads_dict[v2_labl]

        if isOverlap(v1_read, v2_read, k):
            adjacency_list.append((v1_labl.strip(">"), v2_labl.strip(">")))
        if isOverlap(v2_read, v1_read, k):
            adjacency_list.append((v2_labl.strip(">"), v1_labl.strip(">")))

        else:
            continue

    for i in adjacency_list:
        print(i[0], i[1])


overlap_graph(reads_dict, 3)