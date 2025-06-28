#Group membership frequency per geographic population
import pandas as pd
ngrp = 7 #number of groups
output = open('freq_7grp.txt','w') #open file
data = pd.read_excel("dapc_groups.xlsx") #read metadata
freq_grp=data[["pop","DAPC_7g"]] #subset populations
popul=data['pop'] #populations
pop=[] #vector of populations 
for el in range(len(popul)):
    if popul[el] not in pop:
        pop.append(popul[el])
for r in pop:
    filteredPop = freq_grp.loc[freq_grp["pop"]==r] 
    row = r + '\t'
    for i in range(1, ngrp + 1):
        filterGroup = filteredPop.loc[freq_grp["DAPC_7g"]==i] 
        row+= str(len(filterGroup)) + '\t'
    print(row)
    output.write(row+'\n')
    output.flush()
output.close()