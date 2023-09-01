#Count how many individuals in each group per geographical population
import pandas as pd
output = open('C:/Users/Rajiv/Documents/halyomorpha/7g_freq.txt','w') #open file
data = pd.read_excel("C:/Users/Rajiv/Documents/halyomorpha/halys_dapc_groups.xlsx") #read metadata
freq_grp=data[["pop DAPC","DAPC_7g"]] #subset populations
popul=data['pop DAPC'] #populations
pop=[] #populations vector
ngruppi = 7 #number of groups
for el in range(len(popul)):
    if popul[el] not in pop:
        pop.append(popul[el])
for r in pop:
    filteredPop = freq_grp.loc[freq_grp["pop DAPC"]==r] 
    riga = r + '\t'
    for i in range(1, ngruppi + 1):
        filterGroup = filteredPop.loc[freq_grp["DAPC_7g"]==i] 
        riga+= str(len(filterGroup)) + '\t'
    print(riga)
    output.write(riga+'\n')
    output.flush()
output.close()