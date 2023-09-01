#Add groups to correspoinding individuals in excel dataset
import pandas as pd
data = pd.read_excel("HpGP_coancestry_populations_Oct21.xlsx") #open excel file
groups = pd.read_table("kmeans_groups_6.txt") #open group file
id_ex = data["STRAIN_ID"]
g=groups["x"]
a=[]
p=[]
for r in id_ex:
    a.append(str(r))    
for j in a:
    if j in g:
        p.append(g[j])
    else: p.append("abs")
data.insert(6, "DAPC groups", p, True)
data.to_excel("HpGP_coancestry_populations_Oct21_6_groups.xlsx")
