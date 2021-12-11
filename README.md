# Projet_5.1
Les études de métagénomiques mettent en évidence la présence et l'absence de différentes souches dans un microbiome. Pour résumer les abondances, on peut établir des graphes de co-occurence via :  Rapid inference of direct interactions in large-scale ecological networks from heterogeneous microbial sequencing data, Janko Tackmann, Joao Frederico Matias Rodrigues, Christian von Mering. bioRxiv 390195; doi : https://doi.org/10.1101/390195  .

Cependant, ces techniques reposent sur des corrélations et non sur des causalités. Elles ne permettent pas de comprendre les interactions entre organismes. Pour cela, il est important d'intégrer une autre dimension comme les informations contenues dans les réseaux métaboliques des bactéries. 

Pour cela, certaines bases de données existent :  Brunk E, Sahoo S, Zielinski DC, Altunkaya A, Dräger A, Mih N, et al. Recon3D enables a three-dimensional view of gene variation in human metabolism. Nat Biotechnol. Nature Publishing Group; 2018 Mar;36(3):272-81  https://github.com/cdanielmachado/carveme/tree/master/carveme  

Ce projet vise à proposer une stratégie pour détecter les interactions via les échanges de métabolites via Flux Variability Analysis. La stratégie sera a tester sur des données de microbiotes intestinales fournies par le projet HMP.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this repository you will have acces to all our source code. The script folder represents all of the scripts that we used to normalize, compare and perform our FVA, all scripts are numbered according to the order they should be run. In the data folder, each folder are also numbered according to the script they are involved in. In the 7_FVA folder lays all of the FVA that were ran among all of the bacteries models found to match our dataset, finaly the 7_Interactions folder contains only the metabolites within one couple of bacteries that are found to be exchanged.
