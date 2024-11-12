import pandas as pd

def load_and_preprocess_data(file_path):
    """
    Charge et prétraite les données du Titanic
    """
    df = pd.read_csv(file_path)
    
    # Nettoyage des données
    df.dropna(subset=["Age", "Embarked"], inplace=True)
    df["SibSp"] = df["SibSp"] + df["Parch"]
    df.rename(columns={"SibSp": "Relatives"}, inplace=True)
    df.drop(["Name", "Cabin", "Parch"], axis=1, inplace=True)
    
    # Création des sous-dataframes
    df_men = df[(df["Sex"]=="male") & (df["Age"]>=18)]
    df_women = df[(df["Sex"]=="female") & (df["Age"]>=18)]
    df_children = df[df["Age"]<18]
    
    return df, df_men, df_women, df_children