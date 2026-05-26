import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("ESS11e04_1/ESS11e04_1.csv")

df_fr = df.loc[df["cntry"] == "FR"]
df_fr = df_fr[df_fr['lrscale'].between(0, 10)]

df_fr["lrscale"] = abs(df_fr["lrscale"]-5)
df_fr["lrscale"].hist()
plt.xlabel("Position gauche-droite")
plt.title("Distribution du positionnement politique en France")
plt.show()

df_fr["lrscale"].describe()

pol = {}
var = {}



####################################################################
# Polarisation classique
####################################################################
for pays in df["cntry"].unique():
    df_pays = df.loc[df["cntry"] == pays]
    df_pays = df_pays[df_pays['lrscale'].between(0, 10)]
    # df_pays["lrscale"] = abs(df_pays["lrscale"]-5)               
    # print(f"Mean for {pays}: {df_pays['lrscale'].mean()}")
    pol[pays] = df_pays['lrscale'].mean()
    var[pays] = df_pays['lrscale'].std()

pol
var

all = pd.DataFrame.from_dict(pol, orient="index", columns=["Polarisation"])
all = all.sort_values("Polarisation")


all.plot(kind="bar")
plt.xlabel("Pays")
plt.ylabel("Polarisation")
plt.title("Polarisation politique par pays")
plt.show()

####################################################################


all = pd.DataFrame.from_dict(
    pol,
    orient="index",
    columns=["Polarisation"]
)

all["Ecart_type"] = pd.Series(var)

# Remettre les pays comme colonne
all = all.reset_index()

# Renommer
all.columns = ["Pays", "Polarisation", "Ecart_type"]

# Trier par polarisation
all = all.sort_values("Polarisation")


plt.figure(figsize=(10, 12))

plt.errorbar(
    x=all["Polarisation"],      # moyenne
    y=all["Pays"],              # pays
    xerr=all["Ecart_type"],     # écart-type
    fmt='o',                    # point
    color='blue',
    ecolor='gray',
    elinewidth=4,
    capsize=0
)

plt.xlabel("Placement Gauche-Droite")
plt.ylabel("Pays")
plt.title("Polarisation politique par pays")
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()


####################################################################
# Polarisation en valeur absolue --> valeur de réfénce = 5
####################################################################


for pays in df["cntry"].unique():
    df_pays = df.loc[df["cntry"] == pays]
    df_pays = df_pays[df_pays['lrscale'].between(0, 10)]
    df_pays["lrscale"] = abs(df_pays["lrscale"]-5)
    # print(f"Mean for {pays}: {df_pays['lrscale'].mean()}")
    pol[pays] = df_pays['lrscale'].mean()
    var[pays] = df_pays['lrscale'].std()

pol
var

all = pd.DataFrame.from_dict(pol, orient="index", columns=["Polarisation"])
all = all.sort_values("Polarisation")


all.plot(kind="bar")
plt.xlabel("Pays")
plt.ylabel("Polarisation")
plt.title("Polarisation en valeur absolue par pays")
plt.show()



all = pd.DataFrame.from_dict(
    pol,
    orient="index",
    columns=["Polarisation"]
)

all["Ecart_type"] = pd.Series(var)

# Pays comme colonne
all = all.reset_index()

# Renommer
all.columns = ["Pays", "Polarisation", "Ecart_type"]

all = all.sort_values("Polarisation")



plt.figure(figsize=(10, 12))

plt.errorbar(
    x=all["Polarisation"],      # moyenne
    y=all["Pays"],              # pays
    xerr=all["Ecart_type"],     # écart-type
    fmt='o',                    # point
    color='blue',
    ecolor='gray',
    elinewidth=4,
    capsize=0
)

plt.xlabel("Ecart à la position centrale (5)")
plt.ylabel("Pays")
plt.title("Polarisation en valeur absolue par pays")
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()
####################################################################
####################################################################
####################################################################