import sys
input = sys.argv[1]
fasta_file_read = open(input, "r")
count = 0
for f in fasta_file_read.readlines():
    if ">" in f:
        pass
    else:
        count = f.count("-" or "n")
        print(str(count))