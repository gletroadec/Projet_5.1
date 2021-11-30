# script for using FlashWeave

# type closed bracket ( ] ) to open pkg installation options
]
add FlashWeave

#tout en Julia>

using FlashWeave
data_path = "Projet_5.1/Data/2_Transposed .tsv dataset/ERP111526_taxonomy_abundances_SSU_v4.1.tsv"
netw_results = learn_network(data_path, sensitive=true, heterogeneous=false)
G = graph(netw_results)

##save_network("/my/example/network_output.edgelist", netw_results)
save_network("Projet_5.1/Data/3_GML/network_output.gml", netw_results)

## Performance tips
#Depending on your data, make sure to chose the appropriate flags (heterogeneous=true for multi-habitat or -protocol data sets with ideally at least thousands of samples; sensitive=false for faster, but more coarse-grained associations) to achieve optimal runtime. If FlashWeave should get stuck on a small fraction of nodes with large neighborhoods, try increasing the convergence criterion (conv). To learn a network in parallel, see the section below.
#Note, that this package is optimized for large-scale data sets. On small data (hundreds of samples and OTUs) its speed advantages can be negated by JIT-compilation overhead.
