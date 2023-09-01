# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:23:31 2021

@author: Rajiv
"""
#replace gaps - with n
fasta_file_read = open("C:/Users/Rajiv/Documents/mito/mito_2_1r.fasta", "r") #read fasta
fasta_file_new = open("C:/Users/Rajiv/Documents/mito/mito_new_seq_aligned_final.fasta", "w") #write new fasta

for f in fasta_file_read.readlines():
    if ">" in f:
        fasta_file_new.write(f)
    else:
        fasta_file_new.write(f.replace("-", "n"))
fasta_file_read.close()
fasta_file_new.close()