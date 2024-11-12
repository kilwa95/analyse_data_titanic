import matplotlib.pyplot as plt

def set_style():
    """Configure le style des graphiques"""
    plt.style.use("bmh")
    return ["purple", "orange", "green"]

def plot_demographics(df_men, df_women, df_children, colors):
    """Crée le graphique de répartition démographique"""
    plt.figure()
    groupes = ["Hommes", "Femmes", "Enfants"]
    plt.bar("Hommes", df_men["Sex"].value_counts(), label=groupes[0], color=colors[0])
    plt.bar("Femmes", df_women["Sex"].value_counts(), label=groupes[1], color=colors[1])
    plt.bar("Enfants", df_children["Sex"].value_counts(), label=groupes[2], color=colors[2])
    plt.legend(groupes)
    plt.show()

def plot_age_distribution(df):
    """Crée l'histogramme des âges"""
    plt.figure()
    df["Age"].hist(bins=20)
    plt.xlabel("Age")
    plt.ylabel("Fréquence")
    plt.show()

def plot_age_groups(df_men, df_women, df_children, colors):
    """Crée l'histogramme des tranches d'âge par groupe"""
    plt.figure()
    plt.hist([df_men["Age"], df_women["Age"], df_children["Age"]], 
             bins=[0,10,20,30,40,50,60,70,80], color=colors)
    plt.xlabel("Âge")
    plt.ylabel("Fréquence")
    plt.legend(["Hommes", "Femmes", "Enfants"])
    plt.show()

def plot_class_distribution(df_men, df_women, df_children, colors):
    """Crée l'histogramme de distribution des classes"""
    plt.figure()
    plt.hist([df_men["Pclass"], df_women["Pclass"], df_children["Pclass"]], 
             bins=3, color=colors)
    plt.xticks([1,2,3])
    plt.xlabel("Classe")
    plt.ylabel("Fréquence")
    plt.legend(["Hommes", "Femmes", "Enfants"])
    plt.show()