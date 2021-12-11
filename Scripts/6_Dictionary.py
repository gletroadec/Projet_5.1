
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
