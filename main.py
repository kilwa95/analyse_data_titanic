import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv("titanic.csv")

df.dropna(subset=["Age", "Embarked"], inplace=True)
df["SibSp"] = df["SibSp"] + df["Parch"]
df.rename(columns = {"SibSp":"Relatives"}, inplace = True)
df.drop(["Name","Cabin", "Parch"], axis=1, inplace=True)

# Visualisation du jeu de données après nettoyage
print(df.isna().sum())
df.head()
df.describe()



# création de 3 sous-dataframes pour les hommes, femmes et enfants
df_men = df[(df["Sex"]=="male") & (df["Age"]>=18)]
df_women = df[(df["Sex"]=="female") & (df["Age"]>=18)]
df_children = df[df["Age"]<18]

# visualisation graphique de plusieurs données
colors = ["purple","orange","green"]
groupes = ["Hommes", "Femmes", "Enfants"]
plt.style.use("bmh")

# bar plot montrant la répartition hommes/femmes/enfants
plt.figure()
plt.bar("Hommes", df_men["Sex"].value_counts(), label = groupes[0], color = colors[0])
plt.bar("Femmes", df_women["Sex"].value_counts(), label = groupes[1], color = colors[1])
plt.bar("Enfants", df_children["Sex"].value_counts(), label = groupes[2], color = colors[2])
plt.legend(groupes)
plt.show()

# histogramme des âges
plt.figure()
df["Age"].hist(bins=20)
plt.xlabel("Age")
plt.ylabel("Fréquence")
plt.show()

# calcul des tendances centrales pour la colonne "Âge"
mean_age = df["Age"].mean()
median_age = df["Age"].median()
mode_age = df["Age"].mode()
print(f"Âge moyen = {np.round(mean_age, decimals=1)} ans")
print(f"Âge médian = {median_age}")
print(f"Mode = {mode_age} ans")

# histogramme permettant d'observer comment sont répartis les hommes/femmes/enfants par tranches d'âge
plt.figure()
plt.hist( [df_men["Age"],df_women["Age"], df_children["Age"]], bins=[0,10,20,30,40,50,60,70,80] , color = colors )
plt.xlabel("Âge")
plt.ylabel("Fréquence")
plt.legend(["Hommes", "Femmes", "Enfants"])
plt.show()

# histogramme permettant d'observer comment sont répartis les hommes/femmes/enfants par classe
plt.figure()
plt.hist( [df_men["Pclass"],df_women["Pclass"], df_children["Pclass"]], bins = 3, color = colors )
plt.xticks([1,2,3])
plt.xlabel("Classe")
plt.ylabel("Fréquence")
plt.legend(["Hommes", "Femmes", "Enfants"])
plt.show()

# histogramme permettant d'observer s'il y a un lien entre la ville d'embarquement et la classe dans le bateau
plt.figure()
plt.hist( [df[df["Pclass"]==3]["Embarked"], df[df["Pclass"]==2]["Embarked"], df[df["Pclass"]==1]["Embarked"]], bins = 3 )
plt.xticks(ticks=pd.unique(df["Embarked"]))
plt.xlabel("Ville d'embarquement")
plt.ylabel("Fréquence")
plt.margins(x = 0.1)
plt.legend(["3ème", "2ème", "1ère"])
plt.show()

# pie chart permettant d'observer si les passagers voyagaient plutôt seul ou avec des proches
plt.figure()
plt.pie(df["Relatives"].value_counts(), autopct = "%1.1f%%")
plt.legend(["0","1","2","3","4","5","6","7"])
plt.show()