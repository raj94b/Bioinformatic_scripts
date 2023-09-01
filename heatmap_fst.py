#Plot Heatmap for pairwise Fst values
import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_table("fst_matrix.txt")

a.index = range(1,20)
plt.figure()
fig, ax1= plt.subplots(figsize=(10, 10), ncols=1)
plt.title('Fst between groups')
pos = ax1.imshow(a, cmap="RdBu", interpolation="none", extent=[1,19,19,1])
fig.colorbar(pos, ax=ax1)
plt.xticks(range(1,20))
plt.yticks(range(1,20))
plt.savefig("heatmap_fst.pdf")