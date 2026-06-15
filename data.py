import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/raw/ESS11e04_1.csv")
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
plt.xlabel("Auto placement Gauche - Droite")
# plt.title("AutoPlacement idéologique en France")
plt.ylabel("Nombre d'individus")
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














import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/ESS11e04_1.csv")


####################################################################
# Polarisation Idéologique
####################################################################
df = df[df["lrscale"].between(0,10)]

lrscale = df.groupby("cntry")['lrscale'].mean()
polar_idl_std = df.groupby("cntry")['lrscale'].std()


lrscale.plot(kind="bar")
plt.xlabel("Pays")
plt.ylabel("Polarisation")
plt.title("Polarisation politique par pays")
plt.show()

####################################################################

lrscale = pd.concat([lrscale, polar_idl_std], axis=1)
lrscale.columns = ["mean", "std"]
# Remettre les pays comme colonne
lrscale = lrscale.reset_index()

# Renommer

# Trier par polarisation
all = lrscale.sort_values("mean")


plt.figure(figsize=(8, 7))
plt.errorbar(
    x=all["mean"],      # moyenne
    y=all["cntry"],              # pays
    xerr=all["std"],     # écart-type
    fmt='o',                    # point
    color='blue',
    ecolor='gray',
    elinewidth=4,
    capsize=0
)
plt.xlabel("Auto-Placement Gauche-Droite")
plt.ylabel("Pays")
# plt.title("Auto-Placement Gauche-Droite par pays")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()


####################################################################
# Polarisation Idéologique en valeur absolue --> valeur de réfénce = 5
####################################################################
df["polar_idl"] = abs(df["lrscale"]-5)
polar_idl_mean = df.groupby("cntry")['polar_idl'].mean()
polar_idl_std = df.groupby("cntry")['polar_idl'].std()

polar_idl_mean.plot(kind="bar")
plt.xlabel("Pays")
plt.ylabel("Polarisation Idéologique")
plt.title("Polarisation Idéologique par pays")
plt.show()

polar_idl = pd.concat([polar_idl_mean, polar_idl_std], axis=1)
polar_idl.columns = ['mean', 'std']
polar_idl = polar_idl.reset_index()
polar_idl = polar_idl.sort_values("mean")

plt.figure(figsize=(8, 7))
plt.errorbar(
    x=polar_idl["mean"],      # moyenne
    y=polar_idl["cntry"],              # pays
    xerr=polar_idl["std"],     # écart-type
    fmt='o',                    # point
    color='blue',
    ecolor='gray',
    elinewidth=4,
    capsize=0
)
plt.xlabel("Polarisation Idéologique")
plt.ylabel("Pays")
# plt.title("Polarisation Idéologique")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
