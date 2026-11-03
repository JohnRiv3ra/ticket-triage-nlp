import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df = pd.read_csv("data/tickets_en.csv")
X = df["texto"]
y = df["queue"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
vectorizador = TfidfVectorizer()
X_train_tfidf = vectorizador.fit_transform(X_train)
X_test_tfidf = vectorizador.transform(X_test)

print(X_train_tfidf.shape, X_test_tfidf.shape)


modelo = LogisticRegression(max_iter=1000, class_weight="balanced")
modelo.fit(X_train_tfidf, y_train)
predicciones = modelo.predict(X_test_tfidf) 
accuracy = accuracy_score(y_test, predicciones)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, predicciones))
