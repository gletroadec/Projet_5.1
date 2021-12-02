#Création d'un dictionnaire associant nom du noeud au nom du modèle 
model_dictionary = {}
for i in range (len(Pattern)) :
  for node in Test_graph23.nodes : 
    if Pattern[i] in node :
      model_dictionary[node]=pattern[i]

#Ce code créé une liste parallèle contenant les couple et le noms de leur modèles
TTest=[]
Testlist = list(Test_graph23.edges)
for i in range(len(Testlist)):
  oui=0
  oui=[]
  #oui=list(Testlist[i])
  oui=Testlist[i]
  oui=list(oui)
  for e in range(len(oui)):
    oui[e]=model_dictionary[oui[e]]
    #oui=list(oui)
    Testlist[i]=oui
