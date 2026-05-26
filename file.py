import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/raw/ESS11e04_1.csv")
pol = {}
var = {}


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


plt.figure(figsize=(10, 12))
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
plt.title("Auto-Placement Gauche-Droite par pays")
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

plt.figure(figsize=(10, 12))
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
plt.title("Polarisation Idéologique")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
