import pandas as pd

def load_tickets(csv_path):
    """Lädt Ticketdaten aus einer CSV-Datei."""
    return pd.read_csv(csv_path)

if __name__ == "__main__":
    # Beispiel: Daten laden
    df = load_tickets("../data/tickets_sample.csv")
    print(df.head())
