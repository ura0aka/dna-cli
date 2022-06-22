import json

# === function to read FASTA file and convert it into a list:
def readFile(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

# === compile our data into separate variables:
#to store file contents in a list (by calling the read_file function)
FASTA_file = readFile("test_many.txt")
#dictionary for labeling our data:
FASTA_dict = {}
#string to hold label of current FASTA text file:
FASTA_label = ""

# print(FASTA_file)


# === clean and prepare our data for further analysis:
#converting FASTA file data into a dictionary:
for line in FASTA_file:
    if ">" in line:
        FASTA_label = line
        FASTA_dict[FASTA_label] = ""
    else:
        FASTA_dict[FASTA_label] += line
# print(FASTA_dict)





# === compiling data results:
# using dictionary comprehension, we will make a new dictionary for results:
# FASTA_dict_result = {key: <function here>(value) for (key, value) in FASTA_dict.items()}
# print(FASTA_dict_result)

# === converting FASTA file to json and export:
# using json, we will now export the results into a new file
# with open("new_fasta.txt", "w") as FASTA_new:
#     FASTA_new.write(json.dumps(FASTA_dict_result))