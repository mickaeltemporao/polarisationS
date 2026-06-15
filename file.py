#### Polarisation en France 

### Préparation des données

## Chargement des packages
import pandas as pd # gestion de dataframe
import matplotlib.pyplot as plt # modélisation graphique
import seaborn as sns # modélisation graphique
from bs4 import BeautifulSoup # permet de parser le codebook ESS
import misc 

## Importation des données
df = pd.read_csv("data/raw/ESS11e04_1.csv") # import des données de l'European Social Survey Vague 11
df
df_fr = df[df["cntry"] == "FR"] # restriction aux données de la France

### Exploration des données 

## À partir du codebook ESS, on sélectionne les variables d'intérêt pour l'analyse de la polarisation politique en France
# lrscale -> Placement on left right scale, échelle de 0 à 10, 0 = Left, 10 = Right

# gincdif -> Government should reduce differences in income levels, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree 
# lrnobed -> Obedience and respect for authority most important virtues children should learn, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree  
# loylead -> Country needs most loyalty towards its leaders, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree

# freehms -> Gays and lesbians free to live life as they wish, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree
# hmsfmlsh -> Ashamed if close family member gay or lesbian, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree
# hmsacld -> Gay and lesbian couples right to adopt children, échelle de 1 à 5, 1 = Strongly agree, 5 = Strongly disagree

# imdfetn -> Allow many/few immigrants of different race/ethnic group from majority, échelle de 1 à 4, 1 = Allow many, 4 = Allow few                    
# imbgeco -> Immigration bad or good for country's economy, échelle de 0 à 10, 0 = Bad, 10 = Good                                    
# imueclt -> Country's cultural life undermined or enriched by immigrants, échelle de 0 à 10, 0 = Undermined, 10 = Enriched                  
# imwbcnt -> Immigrants make country worse or better place to live, échelle de 0 à 10, 0 = Worse, 10 = Better                 

# ccrdprs -> To what extent feel personal responsibility to reduce climate change, échelle de 0 à 10, 0 = Not at all responsible, 10 = Completely responsible                
# wrclmch -> How worried about climate change, écchelle de 1 à 5, 1 = Not at all worried, 5 = Extremely worried

# wsekpwr -> How often women seek to gain power by getting control over men, échelle de 1 à 5, 1 = Never, 5 = Always 
# wexashr -> How often women exaggerate claims of sexual harassment in the workplace, échelle de 1 à 5, 1 = Never, 5 = Always
# wprtbym -> Women should be protected by men, échelle de 1 à 5, 1 = Agree strongly, 5 = Disagree strongly


## Placement gauche-droite en France
# df_fr['lrscale'][df_fr['lrscale'] <= 10].hist()
df_fr['lrscale'].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Placement on left-right scale")
plt.ylabel("Count")
plt.title("Distribution of Left-Right Placement in France")
plt.show()

# Catégories de placement gauche-droite en France
df_fr['labelGD'] = df_fr['lrscale'].map({
    0: "EG", # Extrême Gauche
    1: "G", # Gauche
    2: "G", 
    3: "CG", # Centre Gauche
    4: "CG", 
    5: "C", # Centre
    6: "CD", # Centre Droit
    7: "CD", 
    8: "D", # Droite
    9: "D",
    10: "ED", # Extrême Droite
    77: "NR", # Non Réponse
    88: "NR",
})

# Orodonner les catégories de placement gauche-droite
df_fr["labelGD"] = pd.Categorical(
    df_fr["labelGD"],
    categories= ["EG", "G", "CG", "C", "CD", "D", "ED", "NR"],
    ordered=True
)

# Répartition des individus dans les caractérisations gauche-droite 
df_fr["labelGD"].value_counts().sort_index().plot.bar()


## Traitement des variables


# Regarder répartition sur une variable des différents groupes
df_fr.groupby("labelGD", observed=False)['lrnobed'].mean().plot.bar()

# Gouvernement doit réduire les inégalités
# 2 comme point neutre
df_fr['inequal'] = df_fr['gincdif'].map({
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    7: 2,
    8: 2,
    9: 2
})

# Droits LGBT
# 2 comme point neutre
df_fr['lgbt'] = df_fr['hmsacld'].map({
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    7: 2,
    8: 2,
    9: 2
})

# Traitement des variables d'immigration
# 2 comme point neutre
df_fr['immigr1'] = df_fr['imdfetn'].map({
    1: 0,
    2: 1, 
    3: 3,
    4: 4,
    7: 2,
    8: 2,
    9: 2
})

df_fr['immigr2'] = df_fr['imdfetn'].map({
    1: 0,
    2: 1, 
    3: 3,
    4: 4,
    7: 2,
    8: 2,
    9: 2
})

# 6 comme point neutre
df_fr['immigr3'] = df_fr['imbgeco'].map({
    0: 10,
    1: 9,
    2: 8,
    3: 7,
    4: 6,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
    10: 0,
    77: 5,
    88: 5,
    99: 5
})

df_fr['immigr4'] = df_fr['imwbcnt'].map({
    0: 10,
    1: 9,
    2: 8,
    3: 7,
    4: 6,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
    10: 0,
    77: 5,
    88: 5,
    99: 5
})

# Traitement données sur le feminisme 
# 0 comme point neutre sur ces questions
df_fr['fem1'] = df_fr['wsekpwr'].map({
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    7: 0,
    8: 0,
    9: 0
})

df_fr['fem2'] = df_fr['wexashr'].map({
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    7: 0,
    8: 0,
    9: 0
})

# 2 comme point neutre
df_fr['fem2'] = df_fr['wprtbym'].map({
    1: 4,
    2: 3,
    3: 2,
    4: 1,
    5: 0,
    7: 2,
    8: 2,
    9: 2
})







for label in df_fr["labelGD"].cat.categories:
    print(f"{label} : {df_fr['hmsacld'][df_fr['labelGD'] == label].mean().round(1)} ")


var = ['gincdif','lrnobed','loylead','freehms','hmsfmlsh','hmsacld',
       'imdfetn','imbgeco','imueclt','imwbcnt',
       'ccrdprs','wrclmch','wsekpwr','weasoff','wexashr','wprtbym']

meanvar = (
        df_fr
        .groupby("labelGD", observed=False)[var]
        .mean()
    )

meanvar['gincdif'].plot.bar()



# Voir pour qui les NR ont voté
df_fr[df_fr['labelGD'] == 'NR']['prtvtffr'].value_counts().sort_index().plot.bar()
# En majorité il n'y a pas de réponse

# Confiance des NR dans les partis politiques 
df_fr[df_fr['labelGD'] == 'NR']['trstprt'].value_counts().sort_index().plot.bar()
# Majorité à 0 -> les non répondants n'ont pas de confiance dans les partis politiques 


for label in df_fr["labelGD"].cat.categories:
    print(f"{label} : {df_fr['prtvtffr'][df_fr['labelGD'] == label].mean().round(1)} ")






