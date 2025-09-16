import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def read_csv():
    df = pd.read_csv('data/tickets_sample.csv')
    x = df['description']
    y = df['category']
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(x)
    print(X_vec.toarray())

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    print(df.head())
    print(df['category'].value_counts())


if __name__ == "__main__":
    read_csv()
