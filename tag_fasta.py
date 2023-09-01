# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:53:04 2021

@author: Rajiv
Add tag to fasta file header
"""

fasta_file_read = open("mito.fasta", "r") #open fasta
fasta_file_new = open("C:/Users/Rajiv/Documents/mito/mito_TAGGED.fasta", "w") #tagged fasta
g=open("mito_pop.txt", "r").readlines() #text file with first tag
p=open("mito_period.txt", "r").readlines() #text file with second tag

lines = fasta_file_read.readlines()
a = 0
for r in range(len(lines)):
    if ">" in lines[r]:
        fasta_file_new.write(">"+g[a].replace("\n", "_")+lines[r].replace("\n", "").replace(">", "")+"_"+"("+p[a].replace("\n",")")+"\n")
        a=a+1
    else:
        fasta_file_new.write(lines[r])
fasta_file_read.close()
fasta_file_new.close()