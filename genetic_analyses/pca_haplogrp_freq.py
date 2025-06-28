##Compute haplogroup frequencies per population
import pandas as pd
output = open("haplo_grp_all.txt",'w') #Create file with haplogroup frquencies per population
df=pd.read_csv("mtHaplo.csv", sep=";") #Read file with haplogroup information
hp=df[["Group","Haplogroup"]]
popul=df["Group"]
hapl=df["Haplogroup"]
pop=[]
hap=[]
riga=[]
for el in range(len(popul)):
    if popul[el] not in pop:
        pop.append(popul[el])
for h in range(len(hapl)):
    if hapl[h] not in hap:
        hap.append(hapl[h])
output.write("Pop"+"\t")
for x in hap:
    output.write(x +"\t")
output.write("\n")
for r in pop:
    filteredPop = hp.loc[hp["Group"]==r] 
    riga = str(r) + '\t'
    for i in hap:
        filterGroup = filteredPop.loc[hp["Haplogroup"]==i] 
        riga+= str(len(filterGroup)/len(filteredPop)) + '\t'
    output.write(riga+'\n')
    output.flush()
output.close()
##Perform scaling of haplogroup frequencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
haplogrp=pd.read_table("haplo_grp_all.txt", sep="\t")
haplogrp.index=haplogrp["Pop"]
final_hap=haplogrp.drop(columns=["Pop"])
final_hap.drop(final_hap.columns[final_hap.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
scaler = StandardScaler() 
scaler.fit(final_hap)
Haplogroups_scaled = scaler.transform(final_hap)
pca = PCA(n_components=2)
PC_scores = pd.DataFrame(pca.fit_transform(Haplogroups_scaled), columns = ['PC1', 'PC2'], index=final_hap.index)
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=final_hap.columns)
##Plot results
PC1 = pca.fit_transform(Haplogroups_scaled)[:,0]
PC2 = pca.fit_transform(Haplogroups_scaled)[:,1]
ldngs = pca.components_
scalePC1 = 1.0/(PC1.max() - PC1.min())
scalePC2 = 1.0/(PC2.max() - PC2.min())
features = final_hap.columns

col=['#4363d8','#ffe119','#3cb44b','#e6194b', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#5ba6bd', '#000000'] #color vector
df = pd.DataFrame({"PC1" : PC1 * scalePC1,"PC2" : PC2 * scalePC2, "Pop" : haplogrp["Pop"]})

fig, ax = plt.subplots(figsize=(14, 9))
sns.scatterplot(data=df, x='PC1',y='PC2',hue='Pop', s=200, palette=col)
for i, feature in enumerate(features):
    ax.arrow(0, 0, ldngs[0, i], 
             ldngs[1, i], 
             head_width=0.02, 
             head_length=0.02, 
             color="gray", alpha=0.4)
    ax.text(ldngs[0, i] * 1.05, 
            ldngs[1, i] * 1.05, 
            feature,color="gray", fontsize=15, alpha=0.4)
 
ax.set_xlabel('PC1', fontsize=20)
ax.set_ylabel('PC2', fontsize=20)
ax.set_title('PCA Haplogroup frequencies', fontsize=20)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
ax.figure.savefig('pca_haplo.pdf')
