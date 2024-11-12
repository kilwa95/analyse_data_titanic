import os
from data_processing.preprocessing import load_and_preprocess_data
from visualizations.plots import (set_style, plot_demographics, 
                                plot_age_distribution, plot_age_groups,
                                plot_class_distribution)

def main():
    # Définir le chemin vers le fichier de données
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
    
    # Charger et prétraiter les données
    df, df_men, df_women, df_children = load_and_preprocess_data(data_path)
    
    # Configurer le style des graphiques
    colors = set_style()
    
    # Créer les visualisations
    plot_demographics(df_men, df_women, df_children, colors)
    plot_age_distribution(df)
    plot_age_groups(df_men, df_women, df_children, colors)
    plot_class_distribution(df_men, df_women, df_children, colors)

if __name__ == "__main__":
    main()