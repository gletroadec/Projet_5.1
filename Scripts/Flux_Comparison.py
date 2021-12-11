pip install pyinterval
from interval import interval, inf

file = #charge la table des flux

Range_x=interval([Common_metabolite_flux['x_minimum'][1],Common_metabolite_flux['x_maximum'][1]])
Range_y=interval([Common_metabolite_flux['y_minimum'][1],Common_metabolite_flux['y_maximum'][1]])

Interaction_table= pd.DataFrame(columns=Common_metabolite_flux.columns)
for i in range(len(Common_metabolite_flux)):
  Range_x=interval([Common_metabolite_flux['x_minimum'][i],Common_metabolite_flux['x_maximum'][i]])
  Range_y=interval([Common_metabolite_flux['y_minimum'][i],Common_metabolite_flux['y_maximum'][i]])
  if not Range_x & Range_y and 0 in interval(Range_x[0][1],Range_y[0][0]):
        Interaction_table.append(Common_metabolite_flux.iloc[i])
if len(Interaction_table) > 0 :
   Interaction_table.to_csv('/Projet_5.1/Data/Interaction/FVA_interaction_'+Testlist[i][0].lower()+'_vs_'+Testlist[i][1].lower()+'.csv')
