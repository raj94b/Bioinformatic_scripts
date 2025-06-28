#Create a fasta file with sequence in a single line
import sys
fasta = sys.argv[0]
output = sys.argv[1]
fasta_file_read = open(fasta, "r") #input file
fasta_file_new = open(output, "w") #new fasta

for f in fasta_file_read.readlines():
    if ">" in f:
        fasta_file_new.write(f.replace(">","\n>"))
    else:
        fasta_file_new.write(f.replace("\n",""))
fasta_file_read.close()
fasta_file_new.close()