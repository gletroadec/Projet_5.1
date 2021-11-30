####Python script for comparing matching names in between the dataset's list and Carveme's dataset ####

test = pd.read_csv('/Projet_5.1/Data/4_/models_list_purified.csv', sep='\t')

#Transforme les noms de modèles en liste

test["Name"] = test["organism"].astype(str)+ '_' + test["name"]
Split_test_nodes = test['Name']
Pattern=Split_test_nodes.values.tolist()

#Se Supprimes les doublons
Pattern = set(Pattern)
Pattern = list(Pattern)

#Met la première lettre de chaque espèce en majuscule
for i in range(len(Pattern)) :
  Pattern[i]= Pattern[i].capitalize()

Test_graph = nx.read_gml('/Projet_5.1/Data/3_GML/network_output.gml')
Test_graph23 = nx.read_gml('/Projet_5.1/Data/3_GML/network_output.gml')

#Ce bloc est essentiel pour l'extraction des modeles associés aux noeuds

Chinese_model=0
Chinese_model=[]
for node in Test_graph.nodes() :
  for e in range(len(Pattern)) :
    if Pattern[e] in node :
      Chinese_model.append(node)

#Purifier les nodes associés à un modele
for node in Test_graph.nodes :
  if node not in Chinese_model :
    Test_graph23.remove_node(node)
len(Test_graph23)
