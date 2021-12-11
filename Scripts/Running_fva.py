#Bien faire attention de modifier le path avant le push
for i in range(len(Testlist)) :
    x = cobra.io.read_sbml_model('Projet_5.1/Data/Carveme/Extracted_complete/' + Testlist[i][0].lower() + '.xml.gz')
    y = cobra.io.read_sbml_model('Projet_5.1/Data/Carveme/Extracted_complete/' + Testlist[i][1].lower() + '.xml.gz')
#Chargement des FVA
    fva_modelx = x.summary(fva=0.9)
    fva_modely = y.summary(fva=0.9)
#Peut-être créer une autre liste spécifiques Uptake/secreted
    x_uptake_list = pd.DataFrame(fva_modelx.uptake_flux.metabolite)
    x_secretion_list = pd.DataFrame(fva_modelx.secretion_flux.metabolite)
    y_uptake_list = pd.DataFrame(fva_modely.uptake_flux.metabolite)
    y_secretion_list = pd.DataFrame(fva_modely.secretion_flux.metabolite)

    x_metabolist=pd.DataFrame(list(x_uptake_list['metabolite'])+list(x_secretion_list['metabolite']),columns=['metabolite'])
    y_metabolist=pd.DataFrame(list(y_uptake_list['metabolite'])+list(y_secretion_list['metabolite']),columns=['metabolite'])

#Isolating common metabolites
    common_metabolites=0
    common_metabolites=[]
    for a in x_metabolist['metabolite']:
        for b in y_metabolist['metabolite']:
            if a==b :
                common_metabolites.append(a)
#Accès faux flux et caractérisation de ces derniers construit deux tableaux de flux propres aux deux membres du couple.
#Accès faux flux et caractérisation de ces derniers construit deux tableaux de flux propres aux deux membres du couple.
    x_common_flux_basis=pd.DataFrame(columns=['metabolite','reaction','flux', 'minimum', 'maximum','x_Flux_type'])
    y_common_flux_basis=pd.DataFrame(columns=['metabolite','reaction','flux', 'minimum', 'maximum','y_Flux_type'])
    n=0
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
#On se retrouve alors avec deux tables caractérisants les flux de chaques métabolites au sein de chaque couples, il est maintenant possible de les concaténer pour n'obtenir qu'une table
    Common_metabolites_y_flux=Common_metabolites_y_flux.rename(columns={"flux": "y_flux", "minimum": "y_minimum", "maximum":"y_maximum"})
    Common_metabolites_x_flux=Common_metabolites_x_flux.rename(columns={"flux": "x_flux", "minimum": "x_minimum", "maximum":"x_maximum"})
#merge
    Common_metabolite_flux=pd.merge(Common_metabolites_x_flux,Common_metabolites_y_flux)
    Common_metabolite_flux.to_csv('/Projet_5.1/Data/FVA/FVA_'+Testlist[i][0].lower()+'_vs_'+Testlist[i][1].lower()+'.csv')
    
    Range_x=interval([Common_metabolite_flux['x_minimum'][1],Common_metabolite_flux['x_maximum'][1]])
    Range_y=interval([Common_metabolite_flux['y_minimum'][1],Common_metabolite_flux['y_maximum'][1]])

    Interaction_table= pd.DataFrame(columns=Common_metabolite_flux.columns)
    for f in range(len(Common_metabolite_flux)):
      Range_x=interval([Common_metabolite_flux['x_minimum'][f],Common_metabolite_flux['x_maximum'][f]])
      Range_y=interval([Common_metabolite_flux['y_minimum'][f],Common_metabolite_flux['y_maximum'][f]])
      if not Range_x & Range_y and 0 in interval(Range_x[0][1],Range_y[0][0]):
        Interaction_table.append(Common_metabolite_flux.iloc[f])
    if len(Interaction_table) > 0 :
        Interaction_table.to_csv('/content/drive/MyDrive/Bioinformatrique 2/DATAs/FVA/'+Testlist[i][0].lower()+'_vs_'+Testlist[i][1].lower()+'.csv')



    Interaction_table_=pd.DataFrame(columns=Common_metabolite_flux.columns)
    Interaction_table_flux=Interaction_table
    for flux_interval in range(len(Common_metabolite_flux)) :
      if Common_metabolite_flux['x_flux'][flux_interval] and Common_metabolite_flux['y_flux'][flux_interval] != 0 :
        Flux_range=interval([Common_metabolite_flux['x_flux'][flux_interval],Common_metabolite_flux['y_flux'][flux_interval]])
        if 0 in Flux_range :
          Interaction_table_flux=Interaction_table_flux.append(Common_metabolite_flux.iloc[flux_interval])
    if len(Interaction_table) > 0 :
        Interaction_table.to_csv('/Projet_5.1/Data/Interaction/FVA_interaction_'+Testlist[i][0].lower()+'_vs_'+Testlist[i][1].lower()+'.csv')



#Next_step : determination de l'échelle de probabilité d'intéraction

