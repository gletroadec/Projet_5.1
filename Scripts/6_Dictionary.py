Testlist=list(Test_graph23.edges)
Testlist2=list(Testlist)
for i in range(len(Testlist)):
  for e in range(1):
    Testlist2=list(Testlist2)
    x=Testlist2[i][e]
    x=model_dictionary[x]
    list(x)
    Testlist2[i][e]=list(x)
    