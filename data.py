import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("ESS11e04_1/ESS11e04_1.csv")
df['vote']  

#Trust in political parties
df['trstprt'].describe() 

# Voted last national election 
df['vote'].describe()

df['vote'].hist()

df['lrscale'].hist()

# df = df[df['lrscale'] <= 10]


################# 
clean = df[df['lrscale'].between(0, 10)]

clean.groupby('gndr')['lrscale'].plot.hist(alpha=0.5)

cleanF = clean[clean['gndr'] == 2]
cleanM = clean[clean['gndr'] == 1]

cleanF['lrscale'].hist()
plt.xlabel("Position gauche-droite")
plt.ylabel("Nombre de femmes")
plt.title("Distribution du positionnement politique des femmes en France")
plt.show()

cleanM['lrscale'].hist()
plt.xlabel("Position gauche-droite")
plt.ylabel("Nombre d'hommes")
plt.title("Distribution du positionnement politique des hommes en France")
plt.show()
#################



#################
sns.histplot(df['lrscale'][df['lrscale'].between(0, 10)], bins=11)
plt.xlabel("Gauche - Droite")
plt.title("Polarisation idéologique")
plt.show()
#################



df.loc[df['lrscale'].between(0, 10), "lrscale"].value_counts().sort_index().plot(kind="bar")


#################   Homme/Femme et positionnement politique
sns.histplot(
    data=df[df['lrscale'].between(0, 10)],
    x="lrscale",
    hue="gndr",
    bins=11,
    multiple="dodge",   
    alpha=0.5           
)

plt.xlabel("Positionnement gauche-droite")
plt.ylabel("Nombre d'individus")
plt.title("Positionnement politique selon le genre")

plt.show()
#################

df['gndr'].value_counts()




df['imsmetn'].value_counts()
clean = df[df['imsmetn'] <= 4]
clean['imsmetn'].hist()

clean = df[df['imdfetn'] <= 4]
clean['imdfetn'].hist()


# Social Axis
clean = clean[clean['imdfetn'] <= 4]  #different ethnic groups +
clean = clean[clean['impcntr'] <= 4]  #out of EUropean countries +
clean = clean[clean['imueclt'] <= 10]  #Culture -
clean['imueclt'] = -clean['imueclt']  
clean = clean[clean['lrnobed'] <= 5]  #Authority for children -
clean['lrnobed'] = -clean['lrnobed']
clean = clean[clean['freehms'] <= 5]  #LGBT -
clean['freehms'] = -clean['freehms']

clean['social'] = clean[['imdfetn', 'impcntr', 'imueclt', 'lrnobed', 'freehms']].mean(axis=1)
clean['social'].hist()


# Economic Axis
clean = clean[clean['gincdif'] <= 5]  #economic inequality +

plt.scatter(clean['social'], clean['gincdif'])


sns.scatterplot(
    data=clean,
    x="gincdif",
    y="social",
    alpha=0.4
)

plt.axhline(0, linestyle="--")
plt.axvline(0, linestyle="--")

plt.xlabel("Échelle économique")
plt.ylabel("Échelle sociétale")
plt.title("Carte politique 2D")

plt.show()




################################

franceDF = df[df['region'].str.contains('FR')]
franceDF

# franceDF = franceDF[franceDF['lrscale'].between(0, 10)]
franceDF.loc[franceDF['lrscale'].between(0, 10), "lrscale"].value_counts().sort_index().plot(kind="bar")
franceDF.loc[franceDF['prtvtffr'].between(0, 10), "prtvtffr"].value_counts().sort_index().plot(kind="bar")

franceDF['prtvtffr'].value_counts()

test = [franceDF[col] for col in franceDF if len(franceDF[col].value_counts()) != 1]
frclean = pd.concat(test, axis=1)
frclean
