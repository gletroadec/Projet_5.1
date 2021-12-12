import pandas as pd
df = pd.read_csv("Projet_5.1/Data/1_Chinese_data/ERP111526_taxonomy_abundances_SSU_v4.1.tsv", sep='\t')
df2=df.T
print(df2)
df2.to_csv("Projet_5.1/Data/2_Transposed .tsv dataset/Chinese_data.tsv", sep="\t")