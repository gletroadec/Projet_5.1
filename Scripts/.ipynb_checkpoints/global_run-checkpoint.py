#### Necessary packages ####

import pandas as pd                         #Used to work with DataFrame
!pip install cobra
import cobra.test                           #Used to work with models
import networkx as nx                       #Used to work with Graphs
!pip install pyinterval                     
from interval import interval, inf, imath   #Used to work with intervals

#### TRANSPOSITION ####


#### JULIA ####

]
add FlashWeave



using FlashWeave
data_path = "Projet_5.1/Data/2_Transposed .tsv dataset/ERP111526_taxonomy_abundances_SSU_v4.1.tsv"
netw_results = learn_network(data_path, sensitive=true, heterogeneous=false)
G = graph(netw_results)

save_network("Projet_5.1/Data/3_GML/network_output.gml", netw_results)

#### Python ####

####Python script for comparing matching names in between the dataset's list and Carveme's dataset ####
model = pd.read_csv('/Projet_5.1/Data/4_Normalized_names/models_list_purified.csv', sep='\t') #Load the model list in model
#Create list containing all models names
model["Name"] = model["organism"].astype(str)+ '_' + model["name"]
model = model['Name']
model_pattern=model.values.tolist()
#The following two lines get rids of duplicates
model_pattern = set(model_pattern)
model_pattern = list(model_pattern)
#Set the first letter of model nanme to capital so the pattern can match in nodes name
for i in range(len(model_pattern)) :
  model_pattern[i]= model_pattern[i].capitalize()


#Load the Graph obtained with JULIA and a copy to work with
Study_Graph = nx.read_gml('Projet_5.1/Data/DATAs/3_GML/network_output.gml')
Study_Graph_copy = nx.read_gml('Projet_5.1/Data/DATAs/3_GML/network_output.gml')

#The following lines get rid of nodes with no associated models
Study_Model_list=0
Study_Model_list=[]
for node in Study_Graph.nodes() :
  for models in range(len(model_pattern)) :
    if model_pattern[models] in node :
      Study_Model_list.append(node)
#Purifier les nodes associés à un modele
for node in Study_Graph.nodes :
  if node not in Study_Model_list :
    Study_Graph_copy.remove_node(node)
len(Study_Graph_copy)

#Set True attribute for Micro-organisms with an associated model
G=Study_Graph
nx.set_node_attributes(G, False, name="Type")
for i in G.nodes :
    for model in model_pattern :
        if model in i :
            G.nodes[i]["Type"]=True

#### DICTIONNAIRE ####

#Creating a dictionnary associating node name to its model name
model_dictionary = {}
for i in range (len(model_pattern)) :
  for node in Study_Graph_copy.nodes :
    if model_pattern[i] in node :
      model_dictionary[node]=model_pattern[i]
      
#To permit the specific visualisation of nodes with an associated model in Gephi, the following lines set attribute True on node with associated models
G=Study_Graph
nx.set_node_attributes(G, False, name="Type")
for i in G.nodes :
    for model in model_pattern :
        if model in i :
            G.nodes[i]["Type"]=True
#Write the new graph
nx.write_gml(G, 'Projet_5.1/Data/DATAs/6_Graph_with_attribute/Attribute_Graph.gml', stringizer=None)

#Creation of a list of micro-organisms couple (each edge imply 2 micro-organsims)
#This list is dealing with the model names
Edge_list = list(Study_Graph_copy.edges)
for Edge in range(len(Edge_list)):
  couple=0
  couple=[]
  couple=Edge_list[Edge]
  couple=list(couple)
  for MO in range(len(couple)):
    couple[MO]=model_dictionary[couple[MO]]
    Edge_list[Edge]=couple

#### FVA ####

#Goal of thes lines : running FVA on each MO (that have a model associated) and compare the resulting flux between members of an edge
#The compared fluxes concerns common metabolites potentially uptked or secreted by MO of an edge
for i in range(len(Edge_list)) :
    x = cobra.io.read_sbml_model('Projet_5.1/Data/Carveme/Extracted_complete/' + Edge_list[i][0].lower() + '.xml.gz')
    y = cobra.io.read_sbml_model('Projet_5.1/Data/Carveme/Extracted_complete/' + Edge_list[i][1].lower() + '.xml.gz')
#Loading FVA
    fva_modelx = x.summary(fva=0.9) #The fva is here set at 0.9 but the value can be changed as wished
    fva_modely = y.summary(fva=0.9) #The fva is here set at 0.9 but the value can be changed as wished
#First MO metabolite list
    x_uptake_list = pd.DataFrame(fva_modelx.uptake_flux.metabolite)
    x_secretion_list = pd.DataFrame(fva_modelx.secretion_flux.metabolite)
    x_metabolist=pd.DataFrame(list(x_uptake_list['metabolite'])+list(x_secretion_list['metabolite']),columns=['metabolite'])
 #Second MO metabolite list
    y_uptake_list = pd.DataFrame(fva_modely.uptake_flux.metabolite)
    y_secretion_list = pd.DataFrame(fva_modely.secretion_flux.metabolite)
    y_metabolist=pd.DataFrame(list(y_uptake_list['metabolite'])+list(y_secretion_list['metabolite']),columns=['metabolite'])

#Isolation of common metabolites between the two MO
    common_metabolites=0
    common_metabolites=[]
    for a in x_metabolist['metabolite']:
        for b in y_metabolist['metabolite']:
            if a==b :
                common_metabolites.append(a)


#Isolation of associated flux
    x_common_flux_basis=pd.DataFrame(columns=['metabolite','reaction','flux', 'minimum', 'maximum','x_Flux_type'])
    y_common_flux_basis=pd.DataFrame(columns=['metabolite','reaction','flux', 'minimum', 'maximum','y_Flux_type'])
    n=0                             #The n is used to set the flux type (uptake or secretion) as Flux Type is not a column of model.uptake_flux in cobrapy
    for d in common_metabolites :

        if d in list(x_uptake_list['metabolite']) :
            x_common_flux_basis=x_common_flux_basis.append(fva_modelx.uptake_flux.loc[fva_modelx.uptake_flux['metabolite'] == d])
            Common_metabolites_x_flux=x_common_flux_basis
            Common_metabolites_x_flux['x_Flux_type'][n]='uptake'

        if d in list(x_secretion_list['metabolite']) :
            x_common_flux_basis=x_common_flux_basis.append(fva_modelx.secretion_flux.loc[fva_modelx.secretion_flux['metabolite'] == d])
            Common_metabolites_x_flux=x_common_flux_basis
            Common_metabolites_x_flux['x_Flux_type'][n]='secretion'

        if d in list(y_uptake_list['metabolite']) :
            y_common_flux_basis=y_common_flux_basis.append(fva_modely.uptake_flux.loc[fva_modely.uptake_flux['metabolite'] == d])
            Common_metabolites_y_flux=y_common_flux_basis
            Common_metabolites_y_flux['y_Flux_type'][n]='uptake'

        if d in list(y_secretion_list['metabolite']) :
            y_common_flux_basis=y_common_flux_basis.append(fva_modely.secretion_flux.loc[fva_modely.secretion_flux['metabolite'] == d])
            Common_metabolites_y_flux=y_common_flux_basis
            Common_metabolites_y_flux['y_Flux_type'][n]='secretion'
        n+=1
#Generation of tables containing flux caracteristics associated to each metabolites for MO of the edge
    Common_metabolites_y_flux=Common_metabolites_y_flux.rename(columns={"flux": "y_flux", "minimum": "y_minimum", "maximum":"y_maximum"})
    Common_metabolites_x_flux=Common_metabolites_x_flux.rename(columns={"flux": "x_flux", "minimum": "x_minimum", "maximum":"x_maximum"})
#Fusion of the two tables
    Common_metabolite_flux=pd.merge(Common_metabolites_x_flux,Common_metabolites_y_flux)
    Common_metabolite_flux.to_csv('/Projet_5.1/Data/FVA/FVA_'+Edge_list[i][0].lower()+'_vs_'+Edge_list[i][1].lower()+'.csv')
#Isolation of complementary flux ranges
    Range_x=interval([Common_metabolite_flux['x_minimum'][1],Common_metabolite_flux['x_maximum'][1]])
    Range_y=interval([Common_metabolite_flux['y_minimum'][1],Common_metabolite_flux['y_maximum'][1]])
    Interaction_table= pd.DataFrame(columns=Common_metabolite_flux.columns)
    for f in range(len(Common_metabolite_flux)):
      Range_x=interval([Common_metabolite_flux['x_minimum'][f],Common_metabolite_flux['x_maximum'][f]])
      Range_y=interval([Common_metabolite_flux['y_minimum'][f],Common_metabolite_flux['y_maximum'][f]])
      if not Range_x & Range_y and 0 in interval(Range_x[0][1],Range_y[0][0]):
        Interaction_table.append(Common_metabolite_flux.iloc[f])
    if len(Interaction_table) > 0 :
        Interaction_table.to_csv('/Projet_5.1/Data/7_FVA/FVA_'+Edge_list[i][0].lower()+'_vs_'+Edge_list[i][1].lower()+'.csv')
#Isolation of predicted flux that may be complementary but have overlapping flux ranges
    Interaction_table_=pd.DataFrame(columns=Common_metabolite_flux.columns)
    Interaction_table_flux=Interaction_table
    for flux_interval in range(len(Common_metabolite_flux)) :
      if Common_metabolite_flux['x_flux'][flux_interval] and Common_metabolite_flux['y_flux'][flux_interval] != 0 :
        Flux_range=interval([Common_metabolite_flux['x_flux'][flux_interval],Common_metabolite_flux['y_flux'][flux_interval]])
        if 0 in Flux_range :
          Interaction_table_flux=Interaction_table_flux.append(Common_metabolite_flux.iloc[flux_interval])
    if len(Interaction_table) > 0 :
        Interaction_table.to_csv('/Projet_5.1/Data/7_Interaction/FVA_interaction_'+Edge_list[i][0].lower()+'_vs_'+Edge_list[i][1].lower()+'.csv')

