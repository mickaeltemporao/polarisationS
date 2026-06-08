# gincdif -> economic inequality
# freehms -> LGBT free to live
# hmsfmlsh -> family values
# hmsacld -> lgbt adopt children
# lrnobed -> authority for children
# loylead -> loyalty to country leader
# imsmetn -> allow migrants of same ethnic group                                
# imdfetn -> allow migrants of different ethnic group                            
# impcntr -> allow migrants from poorer countries outside of Europe             
# imbgeco -> immigrants god/bad for economy                                     *****10
# imueclt -> endmined or enriched by other immigrants cultures                  *****10
# imwbcnt -> immigrants make country worse/better place to live                 *****10
# ccnthum -> cause anthropique du réchauffment climatique                       *specific
# ccrdprs -> feel personal reponsability in climate change                      *****10
# wrclmch -> worry about climate change                                         
# wsekpwr -> pense que les femmes veulent prendre le controle sur les hommes    
# weasoff -> women get easily offended
# wexashr -> women exaggerate sexual harassment
# wprtbym -> women should be protected by men

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/ESS11e04_1.csv")
df_fr = df[df["cntry"] == "FR"]


list_var5 = ['gincdif', 'freehms', 'hmsfmlsh', 'hmsacld', 
             'lrnobed', 'loylead', 'imsmetn', 'imdfetn', 
             'impcntr', 'wrclmch', 'wsekpwr', 'weasoff', 
             'wlespdm', 'wexashr', 'wprtbym']

list_var10 = ['imbgeco', 'imueclt', 'imwbcnt', 'ccrdprs'] #, 'ccnthum']

df_fr[list_var10] = df_fr[list_var10].replace([66,77,88,99],pd.NA)
df_fr[list_var10].isna().sum()

df_fr[list_var5] = df_fr[list_var5].replace([7,8,9], pd.NA)



# df_fr['ccnthum'] = df_fr['ccnthum'].replace(55, 10)
# df_fr['ccnthum'].value_counts()

df_fr.describe()


# df_fr['ccnthum'].mean()
# df_fr['ccnthum'].dropna().mean()



# Imputation des valeurs manquantes par la moyenne de chaque variable
# df_fr[list_var5 +list_var10].replace(pd.NA, df_fr[list_var5 +list_var10].mean()).mean()


### REGARDER ccnthum

study = df_fr[list_var5 +list_var10].copy()
# Converti en numérique 
for var in study:
    study[var] = pd.to_numeric(study[var], errors='coerce')

study


study = study.dropna()
study /= study.max()
study.round(1)
# study = abs(study - 0.5)

study = study.round(1)

study.describe()
study['imbgeco'].value_counts().sort_index()

data = pd.DataFrame({
    'mean': study.mean(),
    'std': study.std()
})

data

data.sort_values('mean', inplace=True)

plt.figure(figsize=(10, 5))
plt.errorbar(
    x=data["mean"],       # moyenne
    y=data.index,         # variables
    xerr=data["std"],     # écart-type
    fmt='o',                    # point
    color='blue',
    ecolor='gray',
    elinewidth=4,
    capsize=0
)
plt.xlabel("Placement sur des enjeux sociaux")
plt.ylabel("Enjeux sociaux")
plt.title("")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()




#################################
# Graph Ridgeline plot
#################################

#score de gauche à droite idéologiquement

immi = study['imsmetn'] + study['imdfetn'] + study['impcntr'] + (1 - study['imbgeco']) + (1 - study['imueclt']) + (1 - study['imwbcnt'])
wmn = study['wsekpwr'] + study['weasoff'] + study['wexashr'] + (1 - study['wprtbym'])


sumglob = study['gincdif'] + study['freehms'] +(1 - study['hmsfmlsh']) + study['hmsacld'] + (1 - study['lrnobed']) + (1 - study['loylead']) + (1 - study['wrclmch']) + (1 - study['ccrdprs'])

# Format long pour seaborn
df_long = study.melt(var_name='variable', value_name='value')
df_long

# Création du ridgeline plot
graph = sns.FacetGrid(df_long, 
                      row='variable', 
                      hue='variable', 
                      aspect=8, 
                      height=1.2)
graph.map(sns.kdeplot, 
          'value', 
          fill=True, 
          alpha=0.8, 
          bw_adjust=0.8)

graph.refline(y=0)

plt.show()




(immi/6).hist()
plt.xlabel("Score de reticence à l'immigration")
plt.ylabel("Nombre de répondants")
plt.show()

(wmn/4).hist()
plt.xlabel("Score de porosité à mysognie")
plt.ylabel("Nombre de répondants")



# Création des scores sur l'immigration et la mysoginie
immi = immi / 6
wmn = wmn / 4

immi.hist()
wmn.hist()