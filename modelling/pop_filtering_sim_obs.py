#Filtering simulations or observed data for Low-ABC
import pandas as pd
from itertools import combinations
import sys

# Simulations or observed data
file_input = sys.argv[1]
#Output
file_output = sys.argv[2]
# Number of populations
npop = int(sys.argv[3])
# Number of columns for each comparison
col = 2004
# Populations to be removed
rmpop = list(map(int, sys.argv[4].split(',')))
# Reading
print("Reading input file...")
df = pd.read_table(file_input, sep=" ", header=None)
# Comparisons
pop = list(range(1, npop + 1))  # [1, 2, 3, 4, 5, 6]
comp = list(combinations(pop, 2))   # [(1,2), (1,3), ..., (5,6)]
# Comparisons to be removed
rmblocks = [
    r for r, (a, j) in enumerate(comp)
    if a in rmpop or j in rmpop
]

print(f"Populations to be removed: {rmpop}")
print(f"Total comparisons: {len(comp)}")
print(f"Comparisons to be removed: {[comp[i] for i in rmblocks]}")
# Find columns
rmcols = []
for j in rmblocks:
    start = j * col
    end = (j + 1) * col
    print(f"Removing columns from index {start} to {end - 1}")
    rmcols.extend(df.columns[start:end])

# Remove columns
print(f"Removing {len(rmcols)} columns...")
df_filt = df.drop(columns=rmcols)

# Save output file
df_filt.to_csv(file_output, index=False, header=None, sep=" ")
print(f"Output saved as '{file_output}' with {df_filt.shape[1]} columns.")
