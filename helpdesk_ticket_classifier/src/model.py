from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Beispiel-Funktion für Modelltraining

def train_classifier(df):
    X = df[["description"]]  # Platzhalter, später Text-Vektorisierung
    y = df["category"]
    # TODO: Text-Vektorisierung einbauen
    # X_vec = ...
    # X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)
    # clf = RandomForestClassifier()
    # clf.fit(X_train, y_train)
    # y_pred = clf.predict(X_test)
    # print(classification_report(y_test, y_pred))
    pass
