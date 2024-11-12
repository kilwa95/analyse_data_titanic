import streamlit as st
import os
from data_processing.preprocessing import load_and_preprocess_data
import matplotlib.pyplot as plt

def main():
    st.title("Analyse des données du Titanic")
    
    # Chargement des données
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
    df, df_men, df_women, df_children = load_and_preprocess_data(data_path)
    
    # Affichage des données brutes
    st.header("Données brutes")
    st.dataframe(df)
    
    # Statistiques démographiques
    st.header("Statistiques démographiques")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Nombre d'hommes", len(df_men))
    with col2:
        st.metric("Nombre de femmes", len(df_women))
    with col3:
        st.metric("Nombre d'enfants", len(df_children))
    
    # Filtrer les données
    st.sidebar.header("Filtres")
    age_range = st.sidebar.slider("Âge", 0, 100, (0, 100))
    selected_class = st.sidebar.multiselect("Classe", [1, 2, 3], default=[1, 2, 3])
    filtered_df = df[
        (df["Age"].between(age_range[0], age_range[1])) &
        (df["Pclass"].isin(selected_class))
    ]
    
    # Affichage des données filtrées
    st.header("Données filtrées")
    st.dataframe(filtered_df)

    # Statistiques sur les données filtrées
    st.header("Statistiques sur les données filtrées")
    st.dataframe(filtered_df.describe())

    # Ajout d'un bouton de téléchargement pour les données filtrées
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Télécharger les données filtrées (CSV)",
        data=csv,
        file_name="titanic_filtered.csv",
        mime="text/csv"
    )

    
    
    # Visualisations
    st.header("Visualisations")
    
    # Distribution des âges
    fig, ax = plt.subplots()
    df["Age"].hist(bins=20, ax=ax)
    plt.xlabel("Age")
    plt.ylabel("Fréquence")
    st.pyplot(fig)
    
    # Distribution des classes
    st.subheader("Distribution par classe")
    fig, ax = plt.subplots()
    plt.hist([df_men["Pclass"], df_women["Pclass"], df_children["Pclass"]], 
             bins=3, label=["Hommes", "Femmes", "Enfants"])
    plt.xticks([1,2,3])
    plt.xlabel("Classe")
    plt.ylabel("Fréquence")
    plt.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()