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
for node in Test_graph.nodes :
  if node not in Chinese_model :
    Test_graph23.remove_node(node)
len(Test_graph23)

#Set True attribute for Micro-organisms with an associated model
G=Study_Graph
nx.set_node_attributes(G, False, name="Type")
for i in G.nodes :
    for model in model_pattern :
        if model in i :
            G.nodes[i]["Type"]=True

